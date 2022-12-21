from constants import VALID_KEYS, VALID_VALUES
# --------------------------------------------------------------------------


class ArgumentsChecker:

    @staticmethod
    def is_valid(args: dict):

        if args is None:
            return False

        elif not VALID_KEYS.issubset(set(args)):
            return False

        elif not {args['cmd1'], args['cmd2']}.issubset(
                VALID_VALUES):
            return False

        return True

