# -*- coding: utf-8 -*-
"""Unit Tests for `pycom.cls` module.
"""

__author__ = 'Papavassiliou Vassilis'


import pytest
import pycom.attr


@pytest.fixture(scope='module')
def mock_cls():
    """Mock a class object.
    """

    class MockClass(object):
        pass

    return MockClass


def test_cls_cached_property_pass(mock_cls):
    """Testing `pycom.cls.cached_classproperty` pass.
    """
    mock_cls.cls_prop = pycom.attr.cached_classproperty(
        lambda cls: 'Hi there!'
    )

    assert mock_cls.cls_prop == 'Hi there!'


def test_cached_property_pass(mock_cls):
    """Testing `pycom.cls.cached_property` pass.
    """
    mock_cls.inst_prop = pycom.attr.cached_property(
        lambda cls: 'Hi there!'
    )

    assert mock_cls().inst_prop == 'Hi there!'
