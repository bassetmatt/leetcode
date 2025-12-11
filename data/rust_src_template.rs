#![allow(unused)]
pub struct Solution;

impl Solution {
    pub fn bwa() {}
}

#[cfg(test)]
mod tests {
    use super::*;
    struct TestCase {
        expected: (),
    }

    #[test]
    fn test_solution() {
        let cases = vec![TestCase {}];
        for case in cases {
            println!("Checking this case!");
            let result = Solution::bwa();
            assert_eq!(result, case.expected);
        }
    }
}
