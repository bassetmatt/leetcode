#![allow(unused)]

use std::collections::hash_map;
pub struct Solution;

impl Solution {
    pub fn is_anagram_sort(s: &str, t: &str) -> bool {
        let s_sort = {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort();
            chars
        };
        let t_sort = {
            let mut chars: Vec<char> = t.chars().collect();
            chars.sort();
            chars
        };
        s_sort == t_sort
    }

    pub fn is_anagram_linear(s: &str, t: &str) -> bool {
        let mut map_s = hash_map::HashMap::new();
        for c in s.chars() {
            *map_s.entry(c).or_insert(0) += 1;
        }
        let mut map_t = hash_map::HashMap::new();
        for c in t.chars() {
            *map_t.entry(c).or_insert(0) += 1;
        }
        map_s == map_t
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        let s = "anagram".to_string();
        let t = "nagaram".to_string();
        assert_eq!(Solution::is_anagram_sort(&s, &t), true);
        assert_eq!(Solution::is_anagram_linear(&s, &t), true);
        let s = "rat".to_string();
        let t = "car".to_string();
        assert_eq!(Solution::is_anagram_sort(&s, &t), false);
        assert_eq!(Solution::is_anagram_linear(&s, &t), false);
    }
}
