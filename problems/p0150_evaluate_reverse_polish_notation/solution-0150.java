package p0150_evaluate_reverse_polish_notation;

import java.util.Arrays;
import java.util.Stack;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            switch (token) {
                case "+" -> {
                    int rhs = stack.pop();
                    int lhs = stack.pop();
                    stack.push(lhs+rhs);
                }
                case "-" -> {
                    int rhs = stack.pop();
                    int lhs = stack.pop();
                    stack.push(lhs-rhs);
                }
                case "*" -> {
                    int rhs = stack.pop();
                    int lhs = stack.pop();
                    stack.push(lhs*rhs);
                }
                case "/" -> {
                    int rhs = stack.pop();
                    int lhs = stack.pop();
                    stack.push(lhs/rhs);
                }
                default -> {
                    stack.push(Integer.valueOf(token));
                }
            }
        }
        return stack.pop();
    }
}

class TestCase {
    public String[] tokens;
    public int expected;

    public TestCase(String[] tokens, int expected) {
        this.tokens = tokens;
        this.expected = expected;
    }
}

@SuppressWarnings("unused")
class SolutionTest {
    @Test
    void testBwa() {
        Solution solution = new Solution();
        TestCase[] testCases = new TestCase[] {
            new TestCase(new String[] {"4", "5", "*"}, 20),
            new TestCase(new String[] {"3", "2", "5", "+", "*"}, 21),
            new TestCase(new String[] {"3", "6", "-", "14", "*"}, -42),
        };
        for (TestCase testCase : testCases) {
            System.err.println("Input: " + Arrays.toString(testCase.tokens));
            int result = solution.evalRPN(testCase.tokens);
            System.err.println("Expected: " + testCase.expected + " | Result: " + result);

            assertEquals(result, testCase.expected);
        }
    }
}
