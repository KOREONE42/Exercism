// game-of-life.ts
export class GameOfLife {
  private grid: number[][]

  constructor(matrix: unknown) {
    if (Array.isArray(matrix)) {
      // Deep-copy to avoid mutating the input
      this.grid = (matrix as number[][]).map(row => row.slice())
    } else {
      this.grid = []
    }
  }

  public tick(): number[][] {
    const rows = this.grid.length
    if (rows === 0) return this.grid
    const cols = this.grid[0].length

    const next: number[][] = Array.from({ length: rows }, () =>
      Array.from({ length: cols }, () => 0)
    )

    const dirs = [
      [-1, -1], [-1, 0], [-1, 1],
      [ 0, -1],          [ 0, 1],
      [ 1, -1], [ 1, 0], [ 1, 1],
    ]

    const inBounds = (r: number, c: number) =>
      r >= 0 && r < rows && c >= 0 && c < cols

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        let liveNeighbors = 0
        for (const [dr, dc] of dirs) {
          const nr = r + dr, nc = c + dc
          if (inBounds(nr, nc) && this.grid[nr][nc] === 1) {
            liveNeighbors++
          }
        }

        const cell = this.grid[r][c]
        if (cell === 1) {
          // Any live cell with two or three live neighbors lives on.
          next[r][c] = (liveNeighbors === 2 || liveNeighbors === 3) ? 1 : 0
        } else {
          // Any dead cell with exactly three live neighbors becomes a live cell.
          next[r][c] = (liveNeighbors === 3) ? 1 : 0
        }
      }
    }

    this.grid = next
    return this.grid
  }

  public state(): number[][] {
    // Return a deep copy so external code can’t mutate internal state
    return this.grid.map(row => row.slice())
  }
}
