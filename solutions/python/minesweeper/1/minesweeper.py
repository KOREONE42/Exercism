from typing import List

def solve_minesweeper(board: List[str], mine_char: str = '*', empty_char: str = ' ') -> List[str]:
    if not board:
        return []

    row_length = len(board[0])
    for row in board:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
        for c in row:
            if c != mine_char and c != empty_char:
                raise ValueError("The board is invalid with current input.")

    height = len(board)
    width = row_length

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]

    def count_adjacent_mines(r: int, c: int) -> int:
        return sum(
            0 <= r+dr < height and 0 <= c+dc < width and board[r+dr][c+dc] == mine_char
            for dr, dc in directions
        )

    solved_board = []
    for r in range(height):
        new_row = ''
        for c in range(width):
            if board[r][c] == mine_char:
                new_row += mine_char
            elif board[r][c] == empty_char:
                count = count_adjacent_mines(r, c)
                new_row += str(count) if count > 0 else empty_char
            else:
                raise ValueError("The board is invalid with current input.")
        solved_board.append(new_row)

    return solved_board

def annotate(minefield: List[str]) -> List[str]:
    return solve_minesweeper(minefield, mine_char='*', empty_char=' ')
