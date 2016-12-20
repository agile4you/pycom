# -*- coding: utf-8 -*-
"""`pycom.attr` module.

Python class development toolkit.
"""

__author__ = 'Papavassiliou Vassilis'
__date__ = '2015-12-1'
__version__ = '0.0.1'
__all__ = ['classproperty', 'cached_property', 'cached_classproperty']


import functools


class ClassPropertyDescriptor(object):
    """ClassProperty Descriptor class.

    Straight up stolen from stack overflow Implements class level property
    non-data descriptor.
    """

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, cls=None):
        if cls is None:  # pragma: no cover
            cls = type(obj)
        return self.fget.__get__(obj, cls)()


def classproperty(func):
    """classproperty decorator.
    Using this decorator a class can have a property. Necessary for properties
    that don't need instance initialization. Works exactly the same as a
    normal property.

    Examples:
        >>> class MyClass(object):
        ...     @classproperty
        ...     def my_prop(self):
        ...         return self.__name__ + ' class'
        ...
        >>> MyClass.my_prop
        'MyClass class'
    """
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return ClassPropertyDescriptor(func)


def cached_property(fun):
    """A memorization decorator for class instance properties.

    It implements the default python `property` decorator, with
    the difference that the function result is computed and attached
    to instance as direct attribute. (Lazy loading and caching.)
    """
    @functools.wraps(fun)
    def get(self):
        try:
            return self._cache[fun]
        except AttributeError:
            self._cache = {}
        except KeyError:  # pragma: no cover
            pass
        ret = self._cache[fun] = fun(self)
        return ret
    return property(get)


def cached_classproperty(fun):
    """A memorization decorator for class  properties.

    It implements the above `classproperty` decorator, with
    the difference that the function result is computed and attached
    to class as direct attribute. (Lazy loading and caching.)
    """
    @functools.wraps(fun)
    def get(cls):
        try:
            return cls.__cache[fun]
        except AttributeError:
            cls.__cache = {}
        except KeyError:  # pragma: no cover
            pass
        ret = cls.__cache[fun] = fun(cls)
        return ret
    return classproperty(get)
