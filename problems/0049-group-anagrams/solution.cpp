#include <array>
#include <functional>
#include <string>
#include <vector>
#include <algorithm>
#include <fmt/core.h>
#include <fmt/ranges.h>

namespace std {
    // AI-generated hasher for formula
    template<>
    struct hash<std::array<unsigned char, 26>> {
        size_t operator()(const std::array<unsigned char, 26>& arr) const {
            size_t h = 0;
            for (auto val : arr) {
                h ^= std::hash<unsigned char>{}(val)+0x9e3779b9 + (h << 6) + (h >> 2);
            }
            return h;
        }
    };
}

class Solution {
public:

    size_t hash_string(const std::string& s) {
        std::array<unsigned char, 26> count = { 0 };
        for (char c : s) {
            count[c - 'a']++;
        }
        std::hash<std::array<unsigned char, 26>> hasher;
        return hasher(count);
    }

    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<size_t, std::vector<std::string>> map_groups;
        for (auto& s : strs) {
            size_t hash = Solution::hash_string(s);
            map_groups[hash].push_back(std::move(s));
        }
        std::vector<std::vector<std::string>> groups;
        for (auto& [hash, anagrams] : map_groups) {
            groups.push_back(std::move(anagrams));
        }
        return groups;
    }
};

struct TestCase {
    std::vector<std::string> strs;
    std::vector<std::vector<std::string>> out;
};

int test() {
    Solution solution;
    TestCase test_cases[] = {
        { {"eat","tea","tan","ate","nat","bat"}, { {"bat"}, {"nat","tan"}, {"ate","eat","tea"} } },
        { {""}, { {""} } },
        { {"a"}, { {"a"} } }
    };
    int error_found = 0;
    for (auto& test_case : test_cases) {
        // Sorting
        std::vector<std::vector<std::string>> result = solution.groupAnagrams(test_case.strs);
        for (auto& group : result) {
            std::sort(group.begin(), group.end());
        }
        std::sort(result.begin(), result.end());
        for (auto& group : test_case.out) {
            std::sort(group.begin(), group.end());
        }
        std::sort(test_case.out.begin(), test_case.out.end());
        if (result != test_case.out) {
            fmt::print(stderr,
                "Test failed for input strs: {}. Expected output: {} but got: {}\n",
                test_case.strs,
                fmt::join(test_case.out, " | "),
                fmt::join(result, " | ")
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
