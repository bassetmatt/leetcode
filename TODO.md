# TODO
## High-prio
- [ ] Create a testing framework for C++
- [ ] Create a testing framework for Python

## Mid-prio
- [ ] Add logging for readme command
- [x] Generate a table for the MD file
  - [x] Include columns for each language treated
- [ ] Try to implement generic structure generation for test cases. See [here](#test-data-translation).
    - [ ] Primitive: bool, int, float, char, str?
    - [ ] Arrays
    - [ ] Graphs?
    - [ ] Matrices?
    - [ ] Linked lists?
    - [ ] Tree?



## Details
### Test data translation
Probably will ditch all that for json, not implementing a DSL + parser for test cases (not yet)

Have test cases be written in a sort of custom language to ease automation.\
Idea:
```
I
a [2, 7, 11, 15]
i 9
O
a [0, 1]
```
or
```
I
s car
s rat
O
b false
```
Have it parsed, then translated into language specific code like `a [2, 7, 11, 15]` turn into:
- `std::vector<int> a = std::vector<int>{ 2, 7, 11, 15 };` for C++.
- `let a = vec![2, 7, 11, 15]` for Rust.
- `a = [2, 7, 11, 15]` for python.

See [this](https://support.leetcode.com/hc/en-us/articles/32442719377939-How-to-create-test-cases-on-LeetCode) for data types
