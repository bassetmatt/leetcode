#include <vector>
#include <unordered_set>
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

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    return 0;
}
