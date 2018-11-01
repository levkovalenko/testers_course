import pytest
import sys


@pytest.mark.xfail()
def test_failed():
    assert False


@pytest.mark.xfail(sys.platform != "win64", reason="requires windows 64bit")
def test_failed_for_not_win32_systems():
    assert False


@pytest.mark.skipif(sys.platform != "win64", reason="requires windows 64bit")
def test_skipped_for_not_win64_systems():
    assert False


def test_1():
    print("test_1")


@pytest.mark.critital_tests
def test_2():
    print("test_2")


def test_3():
    print("test_3")
