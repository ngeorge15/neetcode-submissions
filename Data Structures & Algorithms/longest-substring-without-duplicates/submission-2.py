class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        current = set()
        l, r = 0, 1
        current.add(s[l])
        ret = 1

        while r < len(s):
            while s[r] in current:
                current.remove(s[l])
                l += 1

            current.add(s[r])
            ret = max(ret, r - l + 1)
            r += 1
        
        return ret