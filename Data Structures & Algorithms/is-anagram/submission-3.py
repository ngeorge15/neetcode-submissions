class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s) == self.count_chars(t)

    
    def count_chars(self, s):
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        return count
        