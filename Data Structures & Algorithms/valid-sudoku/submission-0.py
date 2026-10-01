class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row, keep track of seen, if repeat -> false
        # check column ""
        # check subbox
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in sub[(i // 3, j // 3)]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                sub[(i // 3, j // 3)].add(num)

        return True
