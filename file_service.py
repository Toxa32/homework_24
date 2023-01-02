"""This file contains a FileService class providing a business logic to work
with user's requests"""
import re
from typing import Optional, Any, Iterable, TextIO
from file_dao import FileDao
# ---------------------------------------------------------------------------


class FileService:
    """The FileService class provides all necessary methods to work with
    user's requests"""
    def __init__(self, dao: FileDao) -> None:
        """Initialization of the FileService"""
        self._dao = dao
        self._result: Optional[Iterable | Any] = None

    def add_new_file(self, filename: str) -> None:
        """This method adds a new filename into Dao

        :param filename: string containing a filename to add
        """
        self._dao.add_filename(filename)

    def filter(self, value: str) -> None:
        """This method serves to process a request to filter data by the given
        value

        :param value: string containing a value to filter
        """
        data = self._get_source()

        self._result = filter(lambda x: value in x, data)

    def filter_by_regex(self, regex: str) -> None:
        """This method serves to process a request to filter data by the given
        regular expression

        :param regex: string containing a regular expression to filter
        """
        data = self._get_source()
        re_validator = re.compile(regex)

        self._result = filter(lambda x: bool(re_validator.search(x)), data)

    def map(self, value: str) -> None:
        """This method serves to process a request for mapping data

        :param value: string containing a column number to receive. All
        strings in file will be split by the space
        """
        data = self._get_source()

        try:
            column = int(value)

        except ValueError:
            column = 0

        self._result = map(lambda x: x.split(' ')[column] + '\n', data)

    def unique(self, value: Optional[Any] = None) -> None:
        """This method serves to process a request to get unique data

        :param value: do nothing in this occasion and was added to provide
        the same interface for all methods in the class
        """
        data = self._get_source()

        self._result = iter(set(data))

    def sort(self, order: str = 'asc') -> None:
        """This method serves to process to sort data in ascending or
        descending order depending on the user choice

        :param order: string containing with rule ('asc', 'desc') to sort data
        """
        if order not in ('asc', 'desc'):
            order = 'asc'

        data = self._get_source()

        self._result = sorted(data, reverse=False if order == 'asc' else True)

    def limit(self, value: str) -> None:
        """This method serves to limit the number of received strings

        :param value: string containing a number of strings to limit output
        """
        data = self._get_source()

        try:
            amount = int(value)

        except ValueError:
            amount = 1

        limited = list(data)[:amount]

        self._result = iter(limited)

    def get_result(self) -> str:
        """This method serves to return the result of the user's request

        :return: string containing the result of whole request
        """
        if self._result:
            result = ''.join(self._result)
            self._result = None
            return result

        return ''

    def _get_source(self) -> Iterable | TextIO:
        """This method serves to choose the source to receive data from

        :return: TextIO object or Iterable depending on it was a first query
        request or not
        """
        if self._result is None:
            data: Iterable | TextIO = self._dao.open()

        else:
            data = self._result

        return data
