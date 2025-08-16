// game-of-life.ts
export class GameOfLife {
  private grid: number[][]

  constructor(matrix: unknown) {
    this.grid = Array.isArray(matrix)
      ? (matrix as number[][]).map(row => [...row])
      : []
  }

  private countNeighbors(r: number, c: number): number {
    const dirs = [-1, 0, 1]
    return dirs.flatMap(dr =>
      dirs.map(dc => (dr === 0 && dc === 0 ? 0 : this.grid[r + dr]?.[c + dc] ?? 0))
    ).reduce((a, b) => a + b, 0)
  }

  public tick(): number[][] {
    this.grid = this.grid.map((row, r) =>
      row.map((cell, c) => {
        const n = this.countNeighbors(r, c)
        if (cell === 1) return n === 2 || n === 3 ? 1 : 0
        return n === 3 ? 1 : 0
      })
    )
    return this.state()
  }

  public state(): number[][] {
    return this.grid.map(row => [...row])
  }
}
