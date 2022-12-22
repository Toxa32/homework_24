"""This file contains the ArgumentChecker class to check arguments provided
by the user"""
from constants import VALID_KEYS, VALID_VALUES
# --------------------------------------------------------------------------


class ArgumentsChecker:
    """The ArgumentChecker class serves to check arguments provided by the
    user"""
    @staticmethod
    def is_valid(args: dict) -> bool:
        """This method checks arguments from user's request

        :param args: an object of dict or MultiDict type containing arguments
        to check

        :return: True if all arguments are valid, False otherwise
        """
        if args is None:
            return False

        elif not VALID_KEYS.issubset(set(args)):
            return False

        elif not {args['cmd1'], args['cmd2']}.issubset(
                VALID_VALUES):
            return False

        return True
