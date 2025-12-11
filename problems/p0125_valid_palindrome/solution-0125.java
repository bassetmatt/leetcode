package p0125_valid_palindrome;

import org.junit.jupiter.api.Test;

class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        if (right == -1) {
            return true;
        }

        while (left <= right) {
            char l_char = s.charAt(left);
            if (!Character.isLetterOrDigit(l_char)) {
                left++;
                continue;
            }
            char r_char = s.charAt(right);
            if (!Character.isLetterOrDigit(r_char)) {
                right--;
                continue;
            }
            l_char = Character.toLowerCase(l_char);
            r_char = Character.toLowerCase(r_char);
            if (l_char != r_char) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}

class TestCase {
    public String s;
    public boolean expected;

    public TestCase(String s, boolean expected){
        this.s =s;
        this.expected = expected;
    }
}

@SuppressWarnings("unused")
class SolutionTest {
    @Test
    void testBwa() {
        Solution solution = new Solution();
        TestCase[] testCases = new TestCase[] {
            new TestCase("A man, a plan, a canal: Panama", true),
            new TestCase("Race a car", false),
            new TestCase("1A", false),
            new TestCase(" ", true),
            new TestCase("", true),
        };
        for (TestCase testCase : testCases) {
            System.err.println("Testing string '" + testCase.s + "', expecting " + testCase.expected);
        }
    }
}
