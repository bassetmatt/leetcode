#include <vector>
#include <unordered_map>
#include <cstdint>
#include <chrono>
#include <algorithm>
#include <random>
#include <iostream>
#include <cassert>

class Solution {
private:
    std::unordered_map<int, uint32_t> count;
    std::vector<int> unique;
public:

    uint32_t random_in_range_incl(uint32_t start, uint32_t end) {
        assert(end - start + 1 != 0);
        return start + rand() % (end - start + 1);
    }

    uint32_t partition(uint32_t left, uint32_t right, uint32_t pivot_index) {
        uint32_t pivot_freq = count[unique[pivot_index]];
        std::swap(unique[pivot_index], unique[right]);

        uint32_t store_index = left;
        for (uint32_t i = left; i <= right; ++i) {
            uint32_t i_freq = count[unique[i]];
            if (i_freq > pivot_freq) {
                std::swap(unique[store_index], unique[i]);
                store_index++;
            }
        }

        std::swap(unique[right], unique[store_index]);

        return store_index;
    }

    void quick_select(uint32_t left, uint32_t right, uint32_t k) {
        if (left >= right) return;

        uint32_t pivot_index = random_in_range_incl(left, right);
        pivot_index = partition(left, right, pivot_index);

        if (k == pivot_index) {
            return;
        } else if (k < pivot_index) {
            quick_select(left, pivot_index - 1, k);
        } else {
            quick_select(pivot_index + 1, right, k);
        }
    }
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        if (k == 0)  return std::vector<int>();
        uint32_t k_ = k;
        count = std::unordered_map<int, uint32_t>();
        unique = std::vector<int>();

        for (int num : nums) {
            if (count.contains(num)) {
                count[num]++;
            } else {
                count[num] = 1;
                unique.push_back(num);
            }
        }

        uint32_t unique_nb = unique.size();

        if (k_ == unique_nb) return unique;

        quick_select(0, unique_nb - 1, k_);
        return std::vector<int>(unique.begin(), unique.begin() + k);
    }
};

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    Solution s = Solution();
    std::vector<int> v = { 1, 2, 3, 1, 2, 1 };
    s.topKFrequent(v, 1);
    return 0;
}
