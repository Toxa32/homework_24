"""This file contains the Request class to easily process user's request"""
from typing import Dict
from file_service import FileService
from models import RequestArgs
# ---------------------------------------------------------------------------


class Request:
    """The Request class provides all necessary methods to process
    user's request"""

    def __init__(self, service: FileService, mapper: Dict[str, str]) -> None:
        """Initialization of the Request class

        :param service: an instance of FileService class
        :param mapper: a dictionary containing mapping data such as
        "user_request": "method"
        """
        self.service = service
        self.mapper = mapper

    def execute(self, request_args: RequestArgs) -> str:
        """This method serves to execute user's request
        :param request_args: a RequestArgs instance with necessary arguments

        :return: the result string of the request execution
        """
        task_1, value_1, task_2, value_2 = self._create(request_args)

        getattr(self.service, task_1)(value_1)
        getattr(self.service, task_2)(value_2)

        return self.service.get_result()

    def _create(self, request_args: RequestArgs) -> tuple:
        """This method prepares first and second command

        :param request_args: a RequestArgs instance with necessary arguments

        :return: a tuple with methods and values to execute
        """

        self.service.add_new_file(request_args.file)

        task_1 = self.mapper[request_args.cmd_1]
        task_2 = self.mapper[request_args.cmd_2]
        value_1 = request_args.value_1
        value_2 = request_args.value_2

        return task_1, value_1, task_2, value_2
