# ============================================================
# 36. Valid Sudoku
# ============================================================
# Determine if a 9x9 Sudoku board is valid. Only the filled cells
# need to be validated according to the following rules:
#   1. Each row must contain the digits 1-9 without repetition.
#   2. Each column must contain the digits 1-9 without repetition.
#   3. Each of the nine 3x3 sub-boxes must contain the digits
#      1-9 without repetition.
#
# Note: A valid board is not necessarily solvable — we only check
# whether the currently filled cells violate any rule.
#
# Example:
#   Input: (see LeetCode 36 for full board)
#   Output: True / False
# ============================================================

from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    box = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board[0])):
            val = board[i][j]

            if val == '.':
                continue

            # Check if val already seen in same row, column, or 3x3 box
            if val in rows[i] or val in cols[j] or val in box[(i // 3, j // 3)]:
                return False

            rows[i].add(val)
            cols[j].add(val)
            box[(i // 3, j // 3)].add(val)

    return True


# ============================================================
# Notes
# ============================================================
# Approach: Hash Sets for Rows, Columns, and Boxes
#   - Use three defaultdict(set) structures to track which digits
#     have been seen in each row, column, and 3x3 sub-box.
#   - For each non-empty cell, check membership in all three sets.
#     If a duplicate is found, return False immediately.
#   - The box key (i//3, j//3) maps each cell to one of the 9
#     sub-boxes:
#       (0,0) (0,1) (0,2)
#       (1,0) (1,1) (1,2)
#       (2,0) (2,1) (2,2)
#
# Complexity:
#   - Time:  O(1) — The board is always 9x9 = 81 cells. Fixed.
#   - Space: O(1) — At most 9 values per set, 27 sets total. Fixed.
#     (If the board were variable m×n, it would be O(m×n).)
# ============================================================


# ---- Tests ----
valid_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]

invalid_board = [
    ["8","3",".",".","7",".",".",".","."],  # 8 here
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],  # and 8 here → same column
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]

assert isValidSudoku(valid_board) == True
assert isValidSudoku(invalid_board) == False
print("All tests passed!")
