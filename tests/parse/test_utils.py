import pytest


from llama_cloud_services.parse.utils import expand_target_pages, partition_pages


def test_expand_target_pages() -> None:
    with pytest.raises(ValueError):
        list(expand_target_pages("x"))
    with pytest.raises(ValueError):
        list(expand_target_pages("1-2-3"))
    with pytest.raises(ValueError):
        list(expand_target_pages("2-1"))
    result = list(expand_target_pages("0,2-3,5,8-10"))
    assert result == [0, 2, 3, 5, 8, 9, 10]


def test_partion_pages() -> None:
    pages = [0, 2, 3, 5, 8, 9, 10]
    with pytest.raises(ValueError):
        list(partition_pages(pages, 0))
    result = list(partition_pages(pages, 3))
    assert result == ["0,2-3", "5,8-9", "10"]

    with pytest.raises(ValueError):
        list(partition_pages(pages, 3, 0))
    result = list(partition_pages(pages, 3, max_pages=5))
    assert result == ["0,2-3", "5,8"]
    result = list(partition_pages(pages, 3, max_pages=10))
    assert result == ["0,2-3", "5,8-9", "10"]
