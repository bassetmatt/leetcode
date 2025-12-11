#include <stack>
#include <vector>
#include <string>
#include <cstdint>
#include <fmt/core.h>
#include <fmt/ranges.h>

#define APPLY_OP(stack, op) { \
    auto rhs = stack.top(); stack.pop(); \
    auto lhs = stack.top(); stack.pop(); \
    stack.push(lhs op rhs); \
}

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int, std::vector<int>> stack = std::stack<int, std::vector<int>>();
        for (auto token : tokens) {
            if (token == "+") {
                APPLY_OP(stack, +);
            } else if (token == "-") {
                APPLY_OP(stack, -);
            } else if (token == "*") {
                APPLY_OP(stack, *);
            } else if (token == "/") {
                APPLY_OP(stack, / );
            } else {
                stack.push(atoi(token.c_str()));
            }
        }
        return stack.top();
    }
};

struct TestCase {
    std::vector<std::string> tokens;
    int expected;
};

int test() {
    Solution solution;
    TestCase test_cases[] = {
        {{"4", "5", "*"}, 20},
        {{"3", "2", "5", "+", "*"}, 21},
        {{"3", "6", "-", "14", "*"}, -42},
    };
    int error_found = 0;
    for (auto& test_case : test_cases) {
        int result = solution.evalRPN(test_case.tokens);
        if (result != test_case.expected) {
            fmt::println(stderr,
                "Test failed with inputs: {}",
                fmt::join(test_case.tokens, ",")
            );
            fmt::println(stderr,
                "Expected {} but got {}",
                test_case.expected, result
            );

            ++error_found;
        }
    }
    return error_found;
}

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    int errors = test();
    if (errors == 0) {
        fmt::println(stderr, "All test cases passed!");
    } else {
        fmt::println(stderr, "{} test case(s) failed.", errors);
        return 1;
    }
    return 0;
}
