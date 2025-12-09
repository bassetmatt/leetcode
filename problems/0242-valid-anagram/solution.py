from dataclasses import dataclass
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Make it default to 0
        char_count = defaultdict(int)
        for i in range(len(s)):
            char_count[s[i]] += 1
            char_count[t[i]] -= 1
        for count in char_count.values():
            if count != 0:
                return False
        return True


@dataclass
class Case:
    s: str
    t: str
    expected: bool


def test_sol() -> None:
    # Ensures that if there are multiple implementations they are all tested
    sol = Solution()
    cases = [
        Case(s="anagram", t="nagaram", expected=True),
        Case(s="rat", t="car", expected=False),
        Case(s="", t="", expected=True),
        Case(s="a", t="b", expected=False),
        Case(s="s", t="s", expected=True),
        Case(s="a", t="aaa", expected=False),
    ]
    for case in cases:
        err = f"Failed for s={case.s}, t={case.t}: expected {case.expected}"
        assert sol.isAnagram(case.s, case.t) == case.expected, err
