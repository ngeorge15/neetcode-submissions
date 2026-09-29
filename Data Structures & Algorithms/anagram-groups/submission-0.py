class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            index = tuple(self.count_chars(s))
            if index in result:
                result[index].append(s)
            else:
                result[index] = [s]

        return list(result.values())


    def count_chars(self, s):
        chars = [0] * 26

        for ch in s:
            chars[ord(ch) - ord("a")] += 1
        
        return chars
