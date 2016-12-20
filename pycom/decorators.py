# -*- coding: utf-8 -*-
"""`pycom.decorators` module.

Python common decorator toolkit.
"""

from functools import wraps


def timer(method):
    """Timer for python callable objects.
    """
    @wraps(method)
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
        return result

    return timed
