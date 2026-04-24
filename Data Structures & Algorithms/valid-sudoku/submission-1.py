from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def row_check():
            for r in range(9):
                seen = set()
                for c in range(9):
                    val = board[r][c]
                    if val == ".":
                        continue
                    elif val in seen:
                        return False
                    else:
                        seen.add(val)
            return True
        def column_check():
            for c in range(9):
                seen = set()
                for r in range(9):
                    val = board[r][c]
                    if val == ".":
                        continue
                    elif val in seen:
                        return False
                    else:
                        seen.add(val)
            return True
        
        def square_check():
            seen = defaultdict(set)
            for r in range(9):
                for c in range(9):
                    box_row = r//3
                    box_col = c//3
                    val = board[r][c]
                    if val == ".":
                        continue
                    elif val in seen[(box_row, box_col)]:
                        return False
                    else:
                        seen[(box_row, box_col)].add(val)
            return True
        if not row_check(): return False
        if not column_check(): return False
        if not square_check(): return False
        return True