from script2.second import merge
import pytest
def test_merge():
    user_info = {
    "first_name": "Amil",
    "last_name": "Alizada"
    }
    expect="Amil Alizada"
    actual= user_info["first_name"] + " " + user_info["last_name"]
    assert expect==actual
