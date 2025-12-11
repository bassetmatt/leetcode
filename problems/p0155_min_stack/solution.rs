#![allow(unused)]

struct StackNode {
    value: i32,
    min_stack: i32,
}
struct MinStack {
    stack: Vec<StackNode>,
    min_stack: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {
    fn new() -> Self {
        Self {
            stack: vec![],
            min_stack: i32::MAX,
        }
    }

    fn push(&mut self, val: i32) {
        let node = StackNode {
            value: val,
            min_stack: self.min_stack,
        };
        self.stack.push(node);
        self.min_stack = self.min_stack.min(val);
    }

    fn pop(&mut self) {
        if let Some(node) = self.stack.pop() {
            self.min_stack = node.min_stack;
        }
    }

    fn top(&self) -> i32 {
        self.stack.last().unwrap().value
    }

    fn get_min(&self) -> i32 {
        self.min_stack
    }
}
