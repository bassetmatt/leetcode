package p0020_valid_parentheses;

import java.util.Objects;
import java.util.Stack;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Character[] opening = new Character[] {'(', '{', '['};
        Character[] closing = new Character[] {')', '}', ']'};
        for (char c : s.toCharArray()) {
            for (int i = 0; i < 3; i++) {
                if (c == opening[i]) {
                    stack.push(c);
                } else if (c == closing[i]) {
                    if (stack.isEmpty() || !Objects.equals(stack.pop(), opening[i])) {
                        return false;
                    }
                }
            }
        }
        return stack.isEmpty();

    }
}

class TestCase {
    String s;
    boolean expected;
}

@SuppressWarnings("unused")
class SolutionTest {
    @Test
    void testIsValid() {
        Solution solution = new Solution();
        TestCase[] testCases = new TestCase[] {
            new TestCase() {{
                s = "()";
                expected = true;
            }},
            new TestCase() {{
                s = "()[]{}";
                expected = true;
            }},
            new TestCase() {{
                s = "(]";
                expected = false;
            }},
            new TestCase() {{
                s = "([)]";
                expected = false;
            }},
            new TestCase() {{
                s = "{[]}";
                expected = true;
            }},
            new TestCase() {{
                s = "";
                expected = true;
            }},
            new TestCase() {{
                s = "}";
                expected = false;
            }},
            new TestCase() {{
                s = "((()))";
                expected = true;
            }},
            new TestCase() {{
                s = "[";
                expected = false;
            }},
        };
        for (TestCase testCase : testCases) {
            // Prints test case info for debugging
            System.err.println("s: " + testCase.s);
            System.err.println("expected: " + testCase.expected);
            assertEquals(testCase.expected, solution.isValid(testCase.s));
        }
    }
}
