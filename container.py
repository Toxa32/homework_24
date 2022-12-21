from file_dao import FileDao
from file_service import FileService
from args_checker import ArgumentsChecker
# -------------------------------------------------------------------------

dao = FileDao()
service = FileService(dao)
checker = ArgumentsChecker()

query = {
    'filter': service.filter,
    'map': service.map,
    'unique': service.unique,
    'sort': service.sort,
    'limit': service.limit
}
