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

    struct TestCase {
        nums: Vec<i32>,
        expected: bool,
    }

    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                nums: vec![1, 2, 3, 1],
                expected: true,
            },
            TestCase {
                nums: vec![1, 2, 3, 4],
                expected: false,
            },
            TestCase {
                nums: vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
                expected: true,
            },
            TestCase {
                nums: vec![],
                expected: false,
            },
            TestCase {
                nums: vec![1],
                expected: false,
            },
        ];
        for case in cases {
            println!("Testing case with nums: {:?}", case.nums);
            let result = Solution::contains_duplicate(case.nums.clone());
            assert_eq!(result, case.expected);
        }
    }
}
