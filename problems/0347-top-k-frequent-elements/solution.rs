#![allow(unused)]

use std::collections::{BinaryHeap, HashMap};
pub struct Solution;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if k == 0 {
            return vec![];
        }
        let mut count = HashMap::new();
        for num in nums {
            *count.entry(num).or_insert(0) += 1;
        }
        let mut heap = BinaryHeap::from(
            count
                .into_iter()
                .map(|(num, cnt)| (cnt, num))
                .collect::<Vec<_>>(),
        );
        (0..k).map(|_| heap.pop().unwrap().1).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        let result = Solution::top_k_frequent(vec![1, 2, 3, 1, 2, 1], 1);
        assert_eq!(result, vec![1]);
    }
}
