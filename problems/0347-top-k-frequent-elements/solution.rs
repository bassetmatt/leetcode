// #![allow(unused)]

use std::{
    collections::{BinaryHeap, HashMap},
    ops::RangeInclusive,
    time::{SystemTime, UNIX_EPOCH},
};

pub struct Solution;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if k == 0 {
            return vec![];
        }
        let mut count = HashMap::new();
        for num in nums {
            count.entry(num).and_modify(|x| *x += 1).or_insert(1_usize);
        }
        let mut heap = BinaryHeap::from(
            count
                .into_iter()
                .map(|(num, cnt)| (cnt, num))
                .collect::<Vec<_>>(),
        );
        (0..k).map(|_| heap.pop().unwrap().1).collect()
    }

    /// Custom random generator since leetcode doesn't allow crates
    fn random_in_range(range: RangeInclusive<usize>) -> usize {
        let seed = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_nanos();
        let (start, end) = (range.start(), range.end());
        let span = end - start + 1;
        start + seed as usize % span
    }

    /// Puts elements with  smaller frequency to the right of the pivot,
    /// those with a higher frequency to the left, and the pivot on the spot
    fn partition(
        unique: &mut [i32],
        count: &HashMap<i32, usize>,
        left: usize,
        right: usize,
        pivot_index: usize,
    ) -> usize {
        let pivot_frequency = {
            let pivot = unique.get(pivot_index).unwrap();
            count.get(pivot).unwrap()
        };

        unique.swap(pivot_index, right);

        // An index that increases every time that a swap is made
        let mut store_index = left;
        for i in left..=right {
            let i_freq = {
                let i_val = unique.get(i).unwrap();
                count.get(i_val).unwrap()
            };
            // If an element is more frequent, it is sent to the left part of the array
            if i_freq > pivot_frequency {
                unique.swap(store_index, i);
                store_index += 1
            }
        }
        // Puts the pivot on the right spot
        unique.swap(right, store_index);
        // Returns pivot position
        store_index
    }

    /// Adaptation of the quickselect (reversed) to get the k most frequent as the first elements
    fn quickselect(
        unique: &mut [i32],
        count: &HashMap<i32, usize>,
        left: usize,
        right: usize,
        k: usize,
    ) {
        if left == right {
            return;
        }
        let mut pivot_index = Solution::random_in_range(left..=right);

        pivot_index = Solution::partition(unique, count, left, right, pivot_index);

        if k == pivot_index {
            // return
        } else if k < pivot_index {
            // Go Left, we need a more procise selection, we have more than k largest
            Solution::quickselect(unique, count, left, pivot_index - 1, k);
        } else {
            // Go Right, we have less than k elements
            Solution::quickselect(unique, count, pivot_index + 1, right, k);
        }
    }

    pub fn top_k_frequent_partition(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if k == 0 {
            return vec![];
        }

        let k = k as usize;
        let mut count = HashMap::new();
        for num in nums {
            count.entry(num).and_modify(|x| *x += 1).or_insert(1_usize);
        }

        let mut unique: Vec<_> = count.keys().copied().collect();
        let unique_nbs = unique.len();

        if k == unique_nbs {
            return unique;
        }

        // Partially sorts the array so that the top k frequent elements are the first k elements
        Solution::quickselect(&mut unique, &count, 0, unique_nbs - 1, k);
        unique.into_iter().take(k).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    struct TestCase {
        nums: Vec<i32>,
        k: i32,
        expected: Vec<i32>,
    }

    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                nums: vec![1, 1, 1, 2, 2, 3],
                k: 2,
                expected: vec![1, 2],
            },
            TestCase {
                nums: vec![1],
                k: 1,
                expected: vec![1],
            },
            TestCase {
                nums: vec![4, 4, 4, 6, 6, 6, 6, 7, 7, 8],
                k: 3,
                expected: vec![6, 4, 7],
            },
            TestCase {
                nums: vec![4, 1, -1, 2, -1, 2, 3],
                k: 2,
                expected: vec![-1, 2],
            },
        ];

        for case in cases {
            println!("Testing case with nums: {:?}, k: {}", case.nums, case.k);
            let mut result = Solution::top_k_frequent_partition(case.nums.clone(), case.k);
            result.sort_unstable();
            let mut expected = case.expected.clone();
            expected.sort_unstable();
            assert_eq!(result, expected);
        }
    }
}
