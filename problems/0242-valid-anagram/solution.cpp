#include <unordered_map>
#include <string>
#include <algorithm>

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

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    return 0;
}
