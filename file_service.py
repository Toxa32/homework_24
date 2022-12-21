from typing import TextIO, Iterable
from flask import abort
from file_dao import FileDao
# ---------------------------------------------------------------------------


class FileService:

    def __init__(self, dao: FileDao) -> None:

        self._dao = dao
        self._result = None

    def add_new_file(self, filename: str) -> None:

        self._dao.add_filename(filename)

    def filter(self, value: str) -> None:

        data = self._get_source()

        self._result = filter(lambda x: value.lower() in x.lower(), data)

    def map(self, column: str) -> None:

        data = self._get_source()

        try:
            column = int(column)

        except ValueError:
            column = 1

        self._result = map(lambda x: x.split(' ')[column] + '\n', data)

    def unique(self, value = None) -> None:

        data = self._get_source()

        self._result = iter(set(data))

    def sort(self, order: str = 'asc') -> None:

        if order not in ('asc', 'desc'):
            order = 'asc'

        data = self._get_source()

        self._result = sorted(data, reverse=False if order == 'asc' else True)

    def limit(self, value: str) -> None:

        data = self._get_source()

        try:
            value = int(value)
        except ValueError:
            value = 1

        try:
            limited = list(data)[:value]
        except IndexError:
            limited = list(data)

        self._result = iter(limited)

    def get_result(self) -> str:

        result = self._result
        self._result = None

        return ''.join(result)

    def _get_source(self) -> TextIO | Iterable:

        if self._result is None:
            try:
                data = self._dao.open()

            except Exception as e:
                print(f'The error {e} was raised during opening the file')
                abort(400, 'Bad request, the file does not exist')
        else:
            data = self._result

        return data
