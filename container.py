"""This file contains instances of different classes to use in another units
avoiding circular import error"""
from file_dao import FileDao
from file_service import FileService
from request import Request
from constants import QUERY
# -------------------------------------------------------------------------

dao = FileDao()
service = FileService(dao)
user_request = Request(service, QUERY)
