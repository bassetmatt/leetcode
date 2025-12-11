#include <vector>
#include <unordered_set>
#include <fmt/core.h>
#include <fmt/ranges.h>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        auto set = std::unordered_set<int>();
        for (auto num : nums) {
            if (!set.insert(num).second) {
                return true;
            }
        }
        return false;
    }
};

struct TestCase {
    std::vector<int> nums;
    bool expected;
};

int test() {
    Solution solution;
    TestCase test_cases[] = {
        { {1, 2, 3, 1}, true },
        { {1, 2, 3, 4}, false },
        { {1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true },
        { {}, false },
        { {1}, false }
    };
    int error_found = 0;
    for (auto& test_case : test_cases) {
        bool result = solution.containsDuplicate(test_case.nums);
        if (result != test_case.expected) {
            fmt::print(stderr,
                "Test failed for input nums: {}. Expected output: {} but got: {}\n",
                fmt::join(test_case.nums, ", "),
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
