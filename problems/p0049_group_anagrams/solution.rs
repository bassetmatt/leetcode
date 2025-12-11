#![allow(unused)]

use std::collections::HashMap;
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};
pub struct Solution;

impl Solution {
    pub fn hash_string(s: &str) -> u64 {
        let mut count = [0u8; 26];
        for c in s.bytes() {
            count[(c - b'a') as usize] += 1;
        }
        let mut hasher = DefaultHasher::new();
        count.hash(&mut hasher);
        hasher.finish()
    }

    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: Vec<Vec<String>> = vec![];
        let mut map_groups: HashMap<u64, Vec<String>> = HashMap::new();

        for string in strs {
            let hash = Solution::hash_string(&string);
            map_groups.entry(hash).or_default().push(string);
        }

        map_groups.into_values().collect()
    }
}

#[cfg(test)]
mod tests {
    use core::str;

    use super::*;
    struct TestCase {
        strs: Vec<String>,
        expected: Vec<Vec<String>>,
    }

    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                strs: vec![
                    "eat".to_string(),
                    "tea".to_string(),
                    "tan".to_string(),
                    "ate".to_string(),
                    "nat".to_string(),
                    "bat".to_string(),
                ],
                expected: vec![
                    vec!["eat".to_string(), "tea".to_string(), "ate".to_string()],
                    vec!["tan".to_string(), "nat".to_string()],
                    vec!["bat".to_string()],
                ],
            },
            TestCase {
                strs: vec!["".to_string()],
                expected: vec![vec!["".to_string()]],
            },
            TestCase {
                strs: vec!["a".to_string()],
                expected: vec![vec!["a".to_string()]],
            },
        ];
        for case in cases {
            println!("Testing case with strs: {:?}", case.strs);
            let mut result = Solution::group_anagrams(case.strs.clone());
            for group in &mut result {
                group.sort();
            }
            result.sort_by(|a, b| a[0].cmp(&b[0]));
            let mut expected = case.expected.clone();
            for group in &mut expected {
                group.sort();
            }
            expected.sort_by(|a, b| a[0].cmp(&b[0]));
            assert_eq!(result, expected);
        }
    }
}
