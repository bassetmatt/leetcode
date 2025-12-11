#include <deque>
#include <string>
#include <vector>
#include <fmt/core.h>
#include <fmt/ranges.h>

class Solution {
public:
    bool isValid(std::string s) {
        std::deque<char> par_stack = std::deque<char>();

        char open[3] = { '(', '[', '{' };
        char close[3] = { ')', ']', '}' };

        for (char c : s) {
            for (int i = 0; i < 3; ++i) {
                if (c == open[i]) {
                    par_stack.push_back(c);
                    break;
                } else if (c == close[i]) {
                    if (par_stack.empty() || par_stack.back() != open[i]) {
                        return false;
                    }
                    par_stack.pop_back();
                    break;
                } else if (i == 2) {
                    return false;
                }
            }
        }
        return par_stack.empty();
    }
};

struct TestCase {
    std::string s;
    bool expected;
};

int test() {
    Solution solution;
    TestCase test_cases[] = {
        { "()", true },
        { "()[]{}", true },
        { "(]", false },
        { "([)]", false },
        { "{[]}", true },
        { "", true },
        { "}", false },
        { "((()))", true },
        { "[", false }
    };
    int error_found = 0;
    for (auto& test_case : test_cases) {
        bool result = solution.isValid(test_case.s);
        if (result != test_case.expected) {
            fmt::print(stderr,
                "Test failed for input s: {}. Expected output: {} but got: {}\n",
                test_case.s,
                test_case.expected,
                result
            );
            ++error_found;
        }
    }
    return error_found;
}

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    int errors = test();
    if (errors == 0) {
        fmt::print(stderr, "All test cases passed!\n");
    } else {
        fmt::print(stderr, "{} test case(s) failed.\n", errors);
        return 1;
    }
    return 0;
}
