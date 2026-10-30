from app.main import get_human_age


def test_should_return_zero_list_with_zero_arguments() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_list_with_no_zero_arguments() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_with_argument_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_convert_second_human_year_at_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_add_cat_year_after_every_four_years_above_24() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_add_dog_year_after_every_five_years_above_24() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_should_convert_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_convert_cat_and_dog_ages_independently() -> None:
    assert get_human_age(15, 29) == [1, 3]
