class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = [set() for _ in range(9)]
        col_seen = [set() for _ in range(9)]
        box_seen = [set() for _ in range(9)]
        result = True
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if board[row][col] != ".":
                    if num in row_seen[row]:
                        return False
                    if num in col_seen[col]:
                        return False
                    box = (row//3) * 3 +(col//3)
                    if num in box_seen[box]:
                        return False
                    row_seen[row].add(num)
                    col_seen[col].add(num)
                    box_seen[box].add(num)
        return True
