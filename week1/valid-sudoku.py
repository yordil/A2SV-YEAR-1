class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def helper(sub):
            myset = set()
            for i in sub:
                if i != ".":
                    if i in myset:
                        return False
                    myset.add(i)
            return True

        # Check rows
        for i in range(9):
            hashmap = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in hashmap:
                    return False
                else:
                    hashmap.add(board[i][j])

        # Check columns
        for i in range(9):
            hashmap = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in hashmap:
                    return False
                else:
                    hashmap.add(board[j][i])

        # Check subgrids
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                subgrid = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                ans = helper(subgrid)
                if not ans:
                    return False

        return True
