from typing import Callable
from solution import Solution


def test_sol() -> None:
    sol = Solution()
    funcs_to_test: list[Callable] = [
        attrib
        for (key, attrib) in sol.__dict__.items()
        if callable(attrib) and not key.startswith("_")
    ]

    for fn in funcs_to_test:
        assert fn([2, 7, 11, 15], 9) == [0, 1]
