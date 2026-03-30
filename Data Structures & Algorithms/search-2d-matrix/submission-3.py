class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS*COLS -1
        while l<=r:
            m = l+ (r-l)//2
            ROW, COL = m//COLS, m%COLS
            if target > matrix[ROW][COL]:
                l=l+1
            elif target < matrix[ROW][COL]:
                r=r-1
            else:
                return True
        return False
        