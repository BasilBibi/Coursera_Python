
class BbbException(Exception):
    pass


def AlwaysRaisesException(n):
    raise Exception


def AlwaysRaiseBbbException(n):
    raise BbbException('')


def RaiseExceptionOnBadInt(n):
    return int(n)
