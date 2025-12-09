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
    struct TestCase {
        s: &'static str,
        t: &'static str,
        expected: bool,
    }
    use std::vec;

    use super::*;
    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                s: "anagram",
                t: "nagaram",
                expected: true,
            },
            TestCase {
                s: "rat",
                t: "car",
                expected: false,
            },
            TestCase {
                s: "",
                t: "",
                expected: true,
            },
            TestCase {
                s: "a",
                t: "b",
                expected: false,
            },
            TestCase {
                s: "s",
                t: "s",
                expected: true,
            },
            TestCase {
                s: "a",
                t: "aaa",
                expected: false,
            },
        ];
        for case in cases {
            println!("Testing s: {}, t: {}", case.s, case.t);
            assert_eq!(Solution::is_anagram_sort(case.s, case.t), case.expected);
            assert_eq!(Solution::is_anagram_linear(case.s, case.t), case.expected);
        }
    }
}
