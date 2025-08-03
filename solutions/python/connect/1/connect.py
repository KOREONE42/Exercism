from collections import deque

class ConnectGame:
    def __init__(self, board):
        """
        Initialize the game board.
        The board is provided as a multiline string.
        Each line corresponds to one row, with tokens separated by whitespace.
        Leading spaces are removed, so the board can be visually indented.
        """
        # Split board into lines and normalize by stripping whitespace and splitting tokens.
        self.board = [row.strip().split() for row in board.strip().splitlines() if row.strip()]
        self.rows = len(self.board)
        self.cols = len(self.board[0]) if self.rows > 0 else 0

    def get_winner(self):
        """
        Determines which player (if any) has made a winning connection.
        'O' wins if there is a continuous path of 'O' from the top to the bottom.
        'X' wins if there is a continuous path of 'X' from the left to the right.
        
        Returns:
            'O' if player O wins,
            'X' if player X wins,
            '' (empty string) if no winning connection exists.
        """
        # Check if player O has a winning connection from top to bottom.
        if self._has_connection('O'):
            return 'O'
        # Check if player X has a winning connection from left to right.
        if self._has_connection('X'):
            return 'X'
        # If neither have a winning path, return an empty string.
        return ""

    def _has_connection(self, player):
        """
        Uses breadth-first search (BFS) to determine if the given player's stones
        form a connected path between the designated edges.
        
        For player 'O': Starts at any 'O' in the top row and seeks to reach the bottom row.
        For player 'X': Starts at any 'X' in the left column and seeks to reach the right column.
        
        Returns:
            True if a winning connection exists; otherwise, False.
        """
        visited = set()
        dq = deque()
        # The six directions for a hex grid.
        directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
        
        if player == 'O':
            # Initialize BFS with all O's on the top row.
            for c in range(self.cols):
                if self.board[0][c] == 'O':
                    dq.append((0, c))
                    visited.add((0, c))
            target_row = self.rows - 1
            
            while dq:
                r, c = dq.popleft()
                if r == target_row:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.board[nr][nc] == 'O' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            dq.append((nr, nc))
            return False

        elif player == 'X':
            # Initialize BFS with all X's on the leftmost column.
            for r in range(self.rows):
                if self.board[r][0] == 'X':
                    dq.append((r, 0))
                    visited.add((r, 0))
            target_col = self.cols - 1
            
            while dq:
                r, c = dq.popleft()
                if c == target_col:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.board[nr][nc] == 'X' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            dq.append((nr, nc))
            return False
        
        return False
