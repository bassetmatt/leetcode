from collections import defaultdict
from typing import Callable


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Make it default to 0
        char_count = defaultdict(int)
        for i in range(len(s)):
            char_count[s[i]] += 1
            char_count[t[i]] -= 1
        for count in char_count.values():
            if count != 0:
                return False
        return True


if __name__ == "__main__":
    Solution.__dict__
    L = [
        func
        for func in dir(Solution)
        if callable(getattr(Solution, func)) and not func.startswith("_")
    ]
    fn: Callable = Solution.__dict__[L[0]]
    print(fn("s", "s"))
    print(fn("anagram", "nagaram"))  # True
    print(fn("rat", "car"))  # False
