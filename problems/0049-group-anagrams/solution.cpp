#include <array>
#include <functional>
#include <string>
#include <vector>


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

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    return 0;
}
