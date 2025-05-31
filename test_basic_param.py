import pytest 
from calculator import add

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (100, 200, 300),
    (10, 5, 15),
]) 

def test_add_param (a,b, expected):
       assert add(a, b) == expected