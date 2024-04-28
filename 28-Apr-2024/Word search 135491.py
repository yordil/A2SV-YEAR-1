# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    stack.append((i, j, 0, set()))

        while stack:
            row, col, index, visited = stack.pop()
            if index == len(word) - 1:
                return True

            visited.add((row, col))
            index += 1

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (
                    0 <= new_row < len(board)
                    and 0 <= new_col < len(board[0])
                    and (new_row, new_col) not in visited
                    and board[new_row][new_col] == word[index]
                ):
                    stack.append((new_row, new_col, index, set(visited)))

        return False

        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
        # def dfs(row , col , visited , res):
        #     if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row , col) in visited:
        #         return 
        #     res += board[row][col]
        #     visited.add((row , col))
        #     if word.find(res) == 0:
        #         if len(word) == len(res):
        #             return True
        #         for i , j in directions:
        #             if dfs(row + i , col+j , visited.copy() , res):
        #                 return True
        #     else:
        #         return 
        #     return False

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #       if dfs(i , j , set() , ""):
        #         return True

        # return False