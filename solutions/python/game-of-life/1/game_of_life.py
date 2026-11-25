def tick(matrix):
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])

    def live_neighbors(r, c):
        return sum(
            matrix[nr][nc]
            for nr in range(max(0, r - 1), min(rows, r + 2))
            for nc in range(max(0, c - 1), min(cols, c + 2))
            if (nr, nc) != (r, c)
        )

    return [
        [
            1 if (n := live_neighbors(r, c)) == 3 or (n == 2 and matrix[r][c]) else 0
            for c in range(cols)
        ]
        for r in range(rows)
    ]