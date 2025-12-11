from dataclasses import dataclass


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = list()
        for token in tokens:
            if token == "+":
                rhs = stack.pop()
                stack[-1] += rhs
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "*":
                rhs = stack.pop()
                stack[-1] *= rhs
            elif token == "/":
                rhs = stack.pop()
                stack.append(int(stack.pop() / rhs))
            else:
                stack.append(int(token))
        return stack.pop()


@dataclass
class TestCase:
    tokens: list[str]
    expected: int


def test_sol() -> None:
    sol = Solution()
    cases = [
        TestCase(["4", "5", "*"], 20),
        TestCase(["3", "2", "5", "+", "*"], 21),
        TestCase(["3", "6", "-", "14", "*"], -42),
    ]
    for case in cases:
        result = sol.evalRPN(case.tokens)
        err_msg = f"Failed test with input {case.tokens}. Expected {case.expected}, got {result}"
        assert result == case.expected, err_msg
