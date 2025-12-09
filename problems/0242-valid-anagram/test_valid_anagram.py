from dataclasses import dataclass
from solution import Solution


@dataclass
class TestCase:
    s: str
    t: str
    expected: bool


def test_sol() -> None:
    # Ensures that if there are multiple implementations they are all tested
    sol = Solution()
    cases = [
        TestCase(s="anagram", t="nagaram", expected=True),
        TestCase(s="rat", t="car", expected=False),
        TestCase(s="", t="", expected=True),
        TestCase(s="a", t="b", expected=False),
        TestCase(s="s", t="s", expected=True),
        TestCase(s="a", t="aaa", expected=False),
    ]
    for case in cases:
        assert sol.isAnagram(case.s, case.t) == case.expected
