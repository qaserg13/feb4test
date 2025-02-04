from enum import nonmember

import pytest



@pytest.fixture()
def before_after():
    print("\nbefore test")
    yield
    print("\nafter test")

def test_demo1():
    assert 1==1


def test_demo2(before_after):
    assert 2==3
