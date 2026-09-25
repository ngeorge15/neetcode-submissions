class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures)
        prev = []
        prev.append([temperatures[0], 0])

        for i in range(1, len(temperatures)):
            while (len(prev) != 0) and (temperatures[i] > prev[-1][0]):
                curr = prev.pop()
                temps[curr[1]] = i - curr[1]
            prev.append([temperatures[i], i])

        return temps



