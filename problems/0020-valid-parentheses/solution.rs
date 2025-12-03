// #![allow(unused)]

use std::collections::{HashMap, VecDeque};
pub struct Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut parenthesis_stack = VecDeque::new();

        let couples: HashMap<char, char> = HashMap::from([(')', '('), (']', '['), ('}', '{')]);
        let open = ['(', '[', '{'];
        let close = [')', ']', '}'];
        for current in s.chars() {
            if open.contains(&current) {
                parenthesis_stack.push_back(current);
            } else if close.contains(&current) {
                // Taking the top element and seeing if it matches
                if let Some(symb) = parenthesis_stack.pop_back() {
                    // If the parenthesis type doesn't match the closing symb, the string isn't valid
                    if couples.get(&current).is_some_and(|x| *x != symb) {
                        return false;
                    }
                // If the stack is empty and a closing symbol arrives, the string isn't valid
                } else {
                    return false;
                }
            } else {
                unreachable!()
            }
        }
        parenthesis_stack.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_solution() {
        let result = Solution::is_valid("[]".to_string());
        assert_eq!(result, true);
    }
}
