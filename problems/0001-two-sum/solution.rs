#![allow(unused)]
pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = std::collections::HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&index) = map.get(&complement) {
                return vec![index as i32, i as i32];
            }
            map.insert(num, i);
        }
        vec![]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    struct TestCase {
        nums: Vec<i32>,
        target: i32,
        expected: Vec<i32>,
    }

    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                nums: vec![2, 7, 11, 15],
                target: 9,
                expected: vec![0, 1],
            },
            TestCase {
                nums: vec![3, 2, 4],
                target: 6,
                expected: vec![1, 2],
            },
            TestCase {
                nums: vec![3, 3],
                target: 6,
                expected: vec![0, 1],
            },
        ];
        for case in cases {
            println!(
                "Testing case with nums: {:?}, target: {}",
                case.nums, case.target
            );
            // Sorts the result to avoid order issues
            let mut result = Solution::two_sum(case.nums.clone(), case.target);
            result.sort();
            let mut expected = case.expected.clone();
            expected.sort();
            assert_eq!(result, expected);
        }
    }
}
