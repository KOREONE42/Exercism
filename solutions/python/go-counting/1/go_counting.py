WHITE = "W"
BLACK = "B"
NONE = ""

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board, where each string represents one row.
                           Each cell is either "B", "W" or " " (empty).
    """
    
    def __init__(self, board):
        # Save board and define dimensions.
        self.board = board
        self.height = len(board)
        self.width = len(board[0]) if self.height > 0 else 0

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on the board.

        Args:
            x (int): Column on the board.
            y (int): Row on the board.

        Returns:
            (str, set): A tuple, the first element being the owner of that area
                        (one of "W", "B", or "" if no one owns it),
                        the second being a set of (x, y) coordinates representing
                        the territory.
                        
        Raises:
            ValueError: If (x, y) is outside the board.
        """
        # Validate coordinate bounds.
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise ValueError("Invalid coordinate")

        # If the coordinate is not empty (i.e. a stone is present), then it is not part of any territory.
        if self.board[y][x] != " ":
            return (NONE, set())
        
        # Initialize sets for visited cells, region coordinates, and bordering stone colors.
        visited = set()
        region = set()
        border_colors = set()

        def dfs(cx, cy):
            # Mark as visited to avoid re-exploration.
            if (cx, cy) in visited:
                return
            visited.add((cx, cy))
            # This cell must be empty because we start on an empty cell.
            region.add((cx, cy))
            # Check the four orthogonal neighbors.
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.board[ny][nx] == " ":
                        dfs(nx, ny)
                    else:
                        border_colors.add(self.board[ny][nx])
                        
        dfs(x, y)
        
        # Determine the owner based on the bordering stones.
        if border_colors == {BLACK}:
            owner = BLACK
        elif border_colors == {WHITE}:
            owner = WHITE
        else:
            owner = NONE

        return (owner, region)

    def territories(self):
        """Find the owners and the territories of the whole board.

        Returns:
            dict(str, set): A dictionary with keys "B", "W", and "".
                            The corresponding values are sets of (x, y) coordinates
                            that belong to that territory.
        """
        # Initialize result dictionary with default empty sets.
        territory_map = {BLACK: set(), WHITE: set(), NONE: set()}
        visited = set()
        
        # Iterate over each cell in the board.
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != " " or (x, y) in visited:
                    continue

                # For an empty cell not yet visited, flood fill to get the region.
                region = set()
                border_colors = set()

                def dfs(cx, cy):
                    if (cx, cy) in visited:
                        return
                    visited.add((cx, cy))
                    region.add((cx, cy))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.board[ny][nx] == " ":
                                dfs(nx, ny)
                            else:
                                border_colors.add(self.board[ny][nx])
                                
                dfs(x, y)
                # Determine owner for the entire region.
                if border_colors == {BLACK}:
                    owner = BLACK
                elif border_colors == {WHITE}:
                    owner = WHITE
                else:
                    owner = NONE
                    
                territory_map[owner] = territory_map[owner].union(region)

        return territory_map
