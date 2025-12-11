#![allow(unused)]
pub struct Solution;

macro_rules! operation {
    ($stack: ident, $op:tt) => {
        let rhs = $stack.pop().unwrap();
        let lhs = $stack.pop().unwrap();
        $stack.push(lhs $op rhs)
    };
}

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = vec![];
        for token in tokens {
            match token.as_str() {
                "+" => {
                    operation!(stack, +);
                }
                "-" => {
                    operation!(stack, -);
                }
                "*" => {
                    operation!(stack, *);
                }
                "/" => {
                    operation!(stack, /);
                }
                _ => stack.push(token.parse::<i32>().unwrap()),
            }
        }
        stack.pop().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    struct TestCase {
        tokens: Vec<String>,
        expected: i32,
    }

    macro_rules! stringify {
        ($vec:expr) => {
            $vec.iter().map(|s| s.to_string()).collect()
        };
    }
    #[test]
    fn test_solution() {
        let cases = vec![
            TestCase {
                tokens: stringify!(vec!["4", "5", "*"]),
                expected: 20,
            },
            TestCase {
                tokens: stringify!(vec!["3", "2", "5", "+", "*"]),
                expected: 21,
            },
            TestCase {
                tokens: stringify!(vec!["3", "6", "-", "14", "*"]),
                expected: -42,
            },
        ];
        for case in cases {
            println!(
                "Testing case with RPN: {:?}, expecting {}",
                case.tokens, case.expected
            );
            let result = Solution::eval_rpn(case.tokens);
            assert_eq!(result, case.expected);
        }
    }
}
