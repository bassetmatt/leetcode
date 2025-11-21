from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
