from functools import wraps
from time import time
from colorama import Style


def _trunc(s, l):
    if len(s) <= l:
        return s
    else:
        suffix = s[-7:]
        return f"{s[:l - 10]}...{suffix}"


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func: {f.__name__} '
              f'args: {_trunc(str(args), 50)} {_trunc(str(kw), 50)} '
              f'{Style.BRIGHT}took: {1000 * (te - ts):2.4f} msec{Style.RESET_ALL}')
        return result

    return wrap
