# import imp
import pytest
import findstring


def test_ispresent():
    assert findstring.ispersent("Al")


def test_nodigit():
    assert findstring.nodigit("N5")
