from dataclasses import dataclass


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


@dataclass
class TestCase:
    s: str
    expected: bool


def test_sol() -> None:
    sol = Solution()
    cases = [
        TestCase(s="()", expected=True),
        TestCase(s="()[]{}", expected=True),
        TestCase(s="(]", expected=False),
        TestCase(s="([)]", expected=False),
        TestCase(s="{[]}", expected=True),
        TestCase(s="", expected=True),
        TestCase(s="}", expected=False),
        TestCase(s="((()))", expected=True),
        TestCase(s="[", expected=False),
    ]
    for case in cases:
        err_msg = f"Failed for s={case.s}: expected {case.expected}"
        assert sol.isValid(case.s) == case.expected, err_msg
