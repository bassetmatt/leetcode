from typing import Callable
from solution import Solution


def test_sol() -> None:
    # Ensures that if there are multiple implementations they are all tested
    sol = Solution()
    funcs_to_test: list[Callable] = [
        attrib
        for (key, attrib) in sol.__dict__.items()
        if callable(attrib) and not key.startswith("_")
    ]

    for fn in funcs_to_test:
        per_fn(fn)


def per_fn(fn: Callable) -> None:
    assert fn(s="s", t="s")
    assert fn("anagram", "nagaram")
    assert not fn("rat", "car")
