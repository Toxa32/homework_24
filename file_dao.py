"""This file contains a FileDao class providing access to the file with
data"""
import os
from typing import TextIO, Optional
from constants import DATA_DIR
# ---------------------------------------------------------------------------


class FileDao:
    """The FileDao class provides access to the data"""
    def __init__(self) -> None:
        """Initialization of the FileDao class

        _filename - a name of file to open. It should be in the data folder
        _file - TextIO object to read data from
        """
        self._filename: str = ''
        self._file: Optional[TextIO] = None

    def add_filename(self, filename: str) -> None:
        """This method adds a filename to the FileDao field

        :param filename: the name of the file to add
        """
        self._filename = os.path.join(DATA_DIR, filename)

    def open(self) -> TextIO:
        """This method opens a file to return its TextIO object

        :returns: a TextIO object to get data from
        """
        if self._file and not self._file.closed:
            self._close()

        fin = open(self._filename, encoding='utf-8')
        self._file = fin

        return fin

    def _close(self) -> None:
        """This is a closed method serving to close TextIO object after
        using"""
        if self._file:
            self._file.close()

    def __repr__(self) -> str:
        """Representation of the FileDao class"""
        return f"FileDao({self._filename})"

    def __del__(self) -> None:
        """Destructor of the FileDao class to close file if application finish
        its work"""

        if self._file:
            self._close()
