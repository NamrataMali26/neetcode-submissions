class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]    
        squares = [set() for _ in range(9)]  

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_no = (r//3) * 3 + (c//3)
                if val == ".":
                    continue

                if val in rows[r] or val in cols[c] or val in squares[box_no]:
                    return False
                rows[r].add(val) 
                cols[c].add(val)
                squares[box_no].add(val) 
        return True  