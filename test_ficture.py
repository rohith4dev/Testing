import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_append(sample_list):
    sample_list.append(6)
    assert sample_list == [1, 2, 3, 4, 5, 6]

def test_list_remove(sample_list):
    sample_list.remove(3)
    assert sample_list == [1, 2, 4, 5]