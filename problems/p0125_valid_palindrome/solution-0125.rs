pub struct Solution;

impl Solution {
    pub fn is_palindrome_sanitize(s: &str) -> bool {
        // println!("s = {}", s);
        let sanitized: Vec<_> = s
            .chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .map(|mut x| x.make_ascii_lowercase())
            .collect();

        if sanitized.is_empty() {
            return true;
        }

        let mut left: i32 = 0;
        let mut right = (sanitized.len() - 1) as i32;

        // println!("Sanitized: {:?}", sanitized);
        while left <= right {
            // println!("L: {} | R: {}", left, right);
            let l_char = sanitized.get(left as usize).unwrap();
            let r_char = sanitized.get(right as usize).unwrap();
            // println!("L: '{}' | R: '{}'", l_char, r_char);
            if l_char != r_char {
                return false;
            } else {
                left += 1;
                right -= 1;
            }
        }
        true
    }

    pub fn is_palindrome(s: &str) -> bool {
        if s.is_empty() {
            return true;
        }
        let s_bytes = s.as_bytes();
        let mut left = 0;
        // Using i32 because otherwise right -= 1 loops and is still >= left
        let mut right = (s_bytes.len() - 1) as i32;

        while left <= right {
            let mut l_char = s_bytes[left as usize] as char;
            if !l_char.is_ascii_alphanumeric() {
                left += 1;
                continue;
            }
            let mut r_char = s_bytes[right as usize] as char;
            if !r_char.is_ascii_alphanumeric() {
                right -= 1;
                continue;
            }
            l_char.make_ascii_lowercase();
            r_char.make_ascii_lowercase();
            if l_char != r_char {
                return false;
            } else {
                left += 1;
                right -= 1;
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    struct TestCase {
        s: String,
        expected: bool,
    }

    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                s: "A man, a plan, a canal: Panama".to_string(),
                expected: true,
            },
            TestCase {
                s: "Race a car".to_string(),
                expected: false,
            },
            TestCase {
                s: "1A".to_string(),
                expected: false,
            },
            TestCase {
                s: " ".to_string(),
                expected: true,
            },
            TestCase {
                s: "".to_string(),
                expected: true,
            },
        ];
        for case in cases {
            println!("Testing string '{}', expecting {}", case.s, case.expected);
            // let result_sani = Solution::is_palindrome_sanitize(&case.s);
            // assert_eq!(result_sani, case.expected);
            let result = Solution::is_palindrome(&case.s);
            assert_eq!(result, case.expected);
        }
    }
}
