#include <vector>
#include <fmt/base.h>
#include <string>

class Solution {
public:
    bool isPalindrome(std::string s) {

        int left = 0;
        int right = s.length() - 1;
        if (right == -1) {
            return true;
        }
        while (left <= right) {
            char l_char = s[left];
            if (!std::isalnum(l_char)) {
                left++;
                continue;
            }
            char r_char = s[right];
            if (!std::isalnum(r_char)) {
                right--;
                continue;
            }
            l_char = std::tolower(l_char);
            r_char = std::tolower(r_char);

            if (l_char != r_char) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
};


struct TestCase {
    std::string s;
    bool expected;
};

int test() {
    Solution solution;
    TestCase test_cases[] = {
        {"A man, a plan, a canal: Panama", true},
        {"Race a car", false},
        {"1A", false},
        {" ", true},
        {"", true},
    };
    int error_found = 0;
    for (auto& test_case : test_cases) {
        bool result = solution.isPalindrome(test_case.s);
        if (result != test_case.expected) {
            fmt::println(stderr,
                "Test failed for string '{}', expected {}",
                test_case.s,
                test_case.expected
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
