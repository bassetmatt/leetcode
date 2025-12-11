from dataclasses import dataclass
from random import randint
from typing import Counter


class Solution:
    unique: list[int]
    count: dict[int, int]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return []
        count = Counter(nums)
        most_common = count.most_common(k)
        return [num for num, freq in most_common]

    def freq(self, idx: int) -> int:
        return self.count[self.unique[idx]]

    def swap_uniq(self, i: int, j: int) -> None:
        self.unique[i], self.unique[j] = self.unique[j], self.unique[i]

    def partition(
        self,
        left: int,
        right: int,
        pivot_index: int,
    ) -> int:
        pivot_freq = self.freq(pivot_index)

        self.swap_uniq(pivot_index, right)

        store_index = left
        for i in range(left, right + 1):
            i_freq = self.freq(i)

            if i_freq > pivot_freq:
                self.swap_uniq(store_index, i)
                store_index += 1
        self.swap_uniq(right, store_index)
        return store_index

    def quickselect(
        self,
        left: int,
        right: int,
        k: int,
    ) -> None:
        if left == right:
            return

        pivot_index = randint(left, right)
        pivot_index = self.partition(left, right, pivot_index)

        if k == pivot_index:
            return
        elif k < pivot_index:
            # Go left, we have too many elements
            self.quickselect(left, pivot_index - 1, k)
        else:
            # Go right, there are more elements to get
            self.quickselect(pivot_index + 1, right, k)

    def topKFrequent_quickselect(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return []
        count = Counter(nums)
        self.count = count
        self.unique = list(count.keys())

        self.quickselect(0, len(self.unique) - 1, k - 1)
        return self.unique[:k]


@dataclass
class TestCase:
    nums: list[int]
    k: int
    expected: list[int]


def test_sol() -> None:
    sol = Solution()
    cases = [
        TestCase(nums=[1, 1, 1, 2, 2, 3], k=2, expected=[1, 2]),
        TestCase(nums=[1], k=1, expected=[1]),
        TestCase(nums=[4, 1, -1, 2, -1, 2, 3], k=2, expected=[-1, 2]),
    ]
    for case in cases:
        err_msg = f"Failed for nums={case.nums}, k={case.k}"
        res = sol.topKFrequent(case.nums, case.k)
        assert sorted(res) == sorted(case.expected), err_msg
        res_qs = sol.topKFrequent_quickselect(case.nums, case.k)
        assert sorted(res_qs) == sorted(case.expected), err_msg
