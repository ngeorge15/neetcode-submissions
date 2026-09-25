class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = {}
        check2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            check1[s[i]] = check1.get(s[i], 0) + 1
            check2[t[i]] = check2.get(t[i], 0) + 1

        if check1 == check2:
            return True
        
        return False