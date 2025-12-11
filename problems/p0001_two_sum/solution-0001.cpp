#include <vector>
#include <unordered_map>
#include <algorithm>
#include <fmt/core.h>
#include <fmt/ranges.h>

class Solution {
public:
    std::vector<int> twoSumOptimized(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> num_map;
        for (unsigned int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (num_map.find(complement) != num_map.end()) {
                return { num_map[complement], static_cast<int>(i) };
            }
            num_map[nums[i]] = i;
        }
        return {};
    }
};

struct TestCase {
    std::vector<int> nums;
    int target;
    std::vector<int> out;
};

int test() {
    Solution solution;
    TestCase test_cases[] = {
        { {2, 7, 11, 15}, 9, {0, 1} },
        { {3, 2, 4}, 6, {1, 2} },
        { {3, 3}, 6, {0, 1} }
    };
    int error_found = 0;
    for (auto& test_case : test_cases) {
        std::vector<int> result = solution.twoSumOptimized(test_case.nums, test_case.target);
        std::sort(result.begin(), result.end());
        std::sort(test_case.out.begin(), test_case.out.end());
        if (result != test_case.out) {

            fmt::println(stderr,
                "Test failed for input nums: {}, target: {}. Expected output: {} but got: {}",
                fmt::join(test_case.nums, ", "),
                test_case.target,
                fmt::join(test_case.out, ", "),
                fmt::join(result, ", ")
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
