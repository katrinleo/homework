import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def get_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(get_data: list[dict]) -> None:
    """тест функции filter_by_state"""
    result = filter_by_state(get_data)
    for r in result:
        assert r["state"] == "EXECUTED"


def test_sort_by_date(get_data: list[dict]) -> None:
    """тест функци sort_by_date"""
    result = sort_by_date(get_data)
    assert result == sorted(get_data, key=lambda x: x["date"], reverse=True)
