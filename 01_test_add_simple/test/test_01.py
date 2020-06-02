from script.first_task import add
import pytest
def test_add():
    given_val=1
    expected = 2
    actual=add(given_val)
    assert expected==actual