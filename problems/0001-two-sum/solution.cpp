#include <vector>
#include <unordered_map>

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

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    return 0;
}
