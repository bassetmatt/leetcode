from dataclasses import dataclass


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left <= right:
            l_char = s[left]
            r_char = s[right]

            l_alph = l_char.isalnum()
            r_alph = r_char.isalnum()

            if not l_alph:
                left += 1
                continue
            if not r_alph:
                right -= 1
                continue
            if l_char == r_char:
                left += 1
                right -= 1
            else:
                return False
        return True


@dataclass
class TestCase:
    s: str
    expect: bool


def test_sol() -> None:
    sol = Solution()
    cases = [
        TestCase("A man, a plan, a canal: Panama", True),
        TestCase("Race a car", False),
        TestCase("1A", False),
        TestCase(" ", True),
        TestCase("", True),
    ]
    for case in cases:
        result = sol.isPalindrome(case.s)
        err_msg = f"Failed test with input: '{case.s}', should be {case.expect}"
        assert result == case.expect, err_msg
