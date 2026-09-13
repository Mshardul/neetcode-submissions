class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # are rows valid? - O(n^2)
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j]!="." and board[i][j] in visited:
                    return False
                visited.add(board[i][j])

        # are cols valid? - O(n^2)
        for j in range(9):
            visited = set()
            for i in range(9):
                if board[i][j]!="." and board[i][j] in visited:
                    return False
                visited.add(board[i][j])

        # are 3*3 squares valid? - O(n^2)
        for sq_row in range(3):
            for sq_col in range(3):
                visited = set()
                for i in range(3*sq_row, 3*(sq_row+1)):
                    for j in range(3*sq_col, 3*(sq_col+1)):
                        if board[i][j]!="." and board[i][j] in visited:
                            return False
                        visited.add(board[i][j])

        return True
