class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        for i in a:
            try:
                b.remove(i)
            except:
                return False
        if len(b) == 0:
            return True
        else: 
            return False