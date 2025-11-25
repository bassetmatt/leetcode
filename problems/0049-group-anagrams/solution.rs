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
    use super::*;
    #[test]
    fn test_solution() {
        let result = Solution::group_anagrams(vec!["a".to_string()]);
        assert_eq!(result, vec![vec!["a".to_string()]]);
    }
}
