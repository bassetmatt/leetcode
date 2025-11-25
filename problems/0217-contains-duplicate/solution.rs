#![allow(unused)]
pub struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = std::collections::HashSet::new();
        for &num in nums.iter() {
            if !set.insert(num) {
                return true;
            }
        }
        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        let result = Solution::contains_duplicate(vec![1, 1]);
        assert_eq!(result, true);
        let result = Solution::contains_duplicate(vec![1, 2, 1]);
        assert_eq!(result, true);
        let result = Solution::contains_duplicate(vec![1, 2]);
        assert_eq!(result, false);
        let result = Solution::contains_duplicate(vec![1]);
        assert_eq!(result, false);
        let result = Solution::contains_duplicate(vec![]);
        assert_eq!(result, false);
        let result = Solution::contains_duplicate(vec![1, 2, 4, 5, 3, 2, 1, 2, 5]);
        assert_eq!(result, true);
    }
}
