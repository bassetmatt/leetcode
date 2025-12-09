#include <unordered_map>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::unordered_map<char, int> char_count;
        // Since both strings are of equal length, we can iterate through both simultaneously
        for (unsigned int i = 0; i < s.length(); ++i) {
            ++char_count[s[i]];
            --char_count[t[i]];
        }
        for (const auto& [_, count] : char_count) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
};

struct TestCase {
    std::string s;
    std::string t;
    bool expected;
};


int test() {
    Solution sol;
    TestCase testcases[] = {
        {"anagram", "nagaram", true},
        {"rat", "car", false},
        {"", "", true},
        {"a", "b", false},
        {"s", "s", true},
        {"a", "aaa", false}
    };

    int error_found = 0;

    for (const auto& test : testcases) {
        bool result = sol.isAnagram(test.s, test.t);
        if (result != test.expected) {
            // Use printf or println in stderr
            std::fprintf(stderr,
                "Test failed for input s: \"%s\", t: \"%s\". Expected %s but got %s.\n",
                test.s.c_str(), test.t.c_str(),
                test.expected ? "true" : "false",
                result ? "true" : "false");

            ++error_found;
        }
    }

    return error_found;
}

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    int errors = test();
    if (errors == 0) {
        std::cout << "All test cases passed!" << std::endl;
    } else {
        std::cerr << errors << " test case(s) failed." << std::endl;
        return 1;
    }
    return 0;
}
