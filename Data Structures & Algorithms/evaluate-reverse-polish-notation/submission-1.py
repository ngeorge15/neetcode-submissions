class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "*", "-", "/"]
        ret = int(tokens[0])
        record = []
        record.append(int(tokens[0]))

        for i in range(1, len(tokens)):
            if tokens[i] in ops:
                op = tokens[i]
                sec = record.pop()
                curr = record.pop()
                if op == "+":
                    curr += sec
                elif op == "*":
                    curr *= sec
                elif op == "-":
                    curr -= sec
                elif op == "/":
                    curr = int(curr/sec)
                record.append(curr)

            else:
                record.append(int(tokens[i]))
        
        return record.pop()