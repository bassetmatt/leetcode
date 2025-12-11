package p0001_two_sum;

import java.util.Arrays;
import java.util.HashMap;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

class TestCase {
    int[] nums;
    int target;
    int[] expected;

    TestCase(int[] nums, int target, int[] expected) {
        this.nums = nums;
        this.target = target;
        this.expected = expected;
    }
}

class SolutionTest {
    // You can run this main method to execute tests manually
    public static void main(String[] args) {
        SolutionTest test = new SolutionTest();
        test.testContainsDuplicate();
        System.out.println("All tests passed!");
    }

    @Test
    void testContainsDuplicate() {
        Solution solution = new Solution();
        TestCase[] testCases = new TestCase[] {
            new TestCase(new int[] {2, 7, 11, 15}, 9, new int[] {0, 1}),
            new TestCase(new int[] {3, 2, 4}, 6, new int[] {1, 2}),
            new TestCase(new int[] {3, 3}, 6, new int[] {0, 1}),
        };
        for (TestCase testCase : testCases) {
            int[] result = solution.twoSum(testCase.nums, testCase.target);
            Arrays.sort(result);
            Arrays.sort(testCase.expected);
            assertArrayEquals(testCase.expected, result);
        }
    }
}
