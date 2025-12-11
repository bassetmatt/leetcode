package p0347_top_k_frequent_elements;

import java.util.Arrays;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

class Solution {

    private int[] unique;
    private HashMap<Integer, Integer> count = new HashMap<>();

    public int[] topKFrequent(int[] nums, int k) {
        if (k == 0) {
            return new int[]{};
        }

        count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> {
            // Difference in frequency
            return b[1] - a[1];
        });

        for (HashMap.Entry<Integer, Integer> entry : count.entrySet()) {
            heap.add(
                    new int[]{(int) entry.getKey(), (int) entry.getValue()}
            );
        }

        // Gets the k most frequent elements
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = heap.poll()[0];
        }
        return result;
    }

    int frequency(int index) {
        int num = unique[index];
        return count.get(num);
    }

    int swap(int i, int j) {
        int temp = unique[i];
        unique[i] = unique[j];
        unique[j] = temp;
        return 0;
    }

    int partition(int left, int right, int pivotIndex) {
        int pivotFreq = frequency(pivotIndex);

        swap(pivotIndex, right);
        int storeIndex = left;
        for (int i = left; i <= right; i++) {
            int iFreq = frequency(i);
            if (iFreq > pivotFreq) {
                swap(storeIndex, i);
                storeIndex++;
            }
        }

        swap(right, storeIndex);
        return storeIndex;
    }

    void quickSelect(int left, int right, int k) {
        if (left == right) {
            return;
        }

        Random rand = new Random();
        int pivotIndex = left + rand.nextInt(right - left + 1);
        pivotIndex = partition(left, right, pivotIndex);
        if (k == pivotIndex) {
            // Found k most frequent elements
        } else if (k < pivotIndex) {
            // Go left, too many elements
            quickSelect(left, pivotIndex - 1, k);
        } else {
            // Go right, not enough elements
            quickSelect(pivotIndex + 1, right, k);
        }
    }

    int[] topKFrequentQuickSelect(int[] nums, int k) {
        if (k == 0) {
            return new int[]{};
        }
        count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        unique = new int[count.size()];
        int index = 0;
        for (int num : count.keySet()) {
            unique[index++] = num;
        }

        quickSelect(0, unique.length - 1, k - 1);

        int[] result = new int[k];
        System.arraycopy(unique, 0, result, 0, k);
        return result;
    }
}

class TestCase {

    int[] nums;
    int k;
    int[] expected;

    TestCase(int[] nums, int k, int[] expected) {
        this.nums = nums;
        this.k = k;
        this.expected = expected;
    }
}

@SuppressWarnings("unused")
class SolutionTest {

    @Test
    void testTopKFrequent() {
        Solution solution = new Solution();
        TestCase[] testCases = new TestCase[]{
            new TestCase(new int[]{1, 1, 1, 2, 2, 3}, 2, new int[]{1, 2}),
            new TestCase(new int[]{1}, 1, new int[]{1}),
            new TestCase(new int[]{4, 1, -1, 2, -1, 2, 3}, 2, new int[]{-1, 2}),};
        for (TestCase testCase : testCases) {
            System.err.println("Input: " + java.util.Arrays.toString(testCase.nums) + " k: " + testCase.k);
            System.err.println("Expected: " + java.util.Arrays.toString(testCase.expected));
            int[] result = solution.topKFrequent(testCase.nums, testCase.k);
            System.err.println("Result: " + java.util.Arrays.toString(result));

            Arrays.sort(result);
            Arrays.sort(testCase.expected);
            assertArrayEquals(testCase.expected, result);

            int[] resultQS = solution.topKFrequentQuickSelect(testCase.nums, testCase.k);
            System.err.println("Result (QS): " + java.util.Arrays.toString(resultQS));
            Arrays.sort(resultQS);
            assertArrayEquals(testCase.expected, resultQS);
        }
    }
}
