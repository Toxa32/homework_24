"""This file contains the Request class to easily process user's request"""
from file_service import FileService
# ---------------------------------------------------------------------------


class Request:
    """The Request class provides all necessary methods to process
    user's request"""

    def __init__(self, service: FileService, mapper: dict) -> None:
        """Initialization of the Request class

        :param service: an instance of FileService class
        :param mapper: a dictionary containing mapping data such as
        "user_request": "method"
        """
        self.service = service
        self.mapper = mapper

    def execute(self, **kwargs) -> str:
        """This method serves to execute user's request
        :param kwargs: keyword arguments to build and execute request

        :return: the result string of the request execution
        """
        task_1, value_1, task_2, value_2 = self._create(**kwargs)

        query_1 = f"self.service.{task_1}(value_1)"
        query_2 = f"self.service.{task_2}(value_2)"

        exec(query_1)
        exec(query_2)

        return self.service.get_result()

    def _create(self, **kwargs):
        """This method prepares first and second command

        :param kwargs: keyword arguments to build and execute request

        :return: a tuple with methods and values to execute
        """

        self.service.add_new_file(kwargs['file'])

        task_1 = self.mapper[kwargs['cmd1']]
        task_2 = self.mapper[kwargs['cmd2']]
        value_1 = kwargs['value1']
        value_2 = kwargs['value2']

        return task_1, value_1, task_2, value_2
