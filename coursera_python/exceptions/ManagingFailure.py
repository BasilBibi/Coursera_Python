
class BbbException(Exception):
    pass


def AlwaysRaisesException(n):
    raise Exception


def AlwaysRaiseBbbException(n):
    raise BbbException('')


def RaiseExceptionOnBadInt(n):
    return int(n)


def FunctionRunner(f, n):
    f(n)


def CatchAndRaise(f, n):
    try:
        f(n)
    except Exception:
        print('CatchAndRaise EXCEPT')
        raise


def CatchAndRaiseNew(f, n):
    try:
        f(n)
    except Exception:
        raise Exception('Raised Exception')


def MultiCatch(f, n):
    try:
        f(n)
    except BbbException:
        print('MultiCatch EXCEPT BbbException')
    except Exception:
        print('MultiCatch EXCEPT Exception')


def MultiCatchInline(f, n):
    try:
        f(n)
    except (Exception, BbbException):
        print('MultiCatchInline EXCEPT')
