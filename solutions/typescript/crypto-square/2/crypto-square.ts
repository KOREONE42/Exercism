export class Crypto {
  private normalized: string;
  private rows: number;
  private cols: number;

  constructor(plainText: unknown) {
    // Normalize input and compute rectangle dimensions
    this.normalized = this.normalize(String(plainText));
    const { rows, cols } = this.getDimensions(this.normalized.length);
    this.rows = rows;
    this.cols = cols;
  }

  get ciphertext(): string {
    const text = this.normalized;
    const length = text.length;
    if (length === 0) return '';

    // Build the grid row by row, padding the last row if needed
    const grid: string[] = [];
    for (let r = 0; r < this.rows; r++) {
      const start = r * this.cols;
      let row = text.slice(start, start + this.cols);
      if (row.length < this.cols) {
        row = row.padEnd(this.cols, ' ');
      }
      grid.push(row);
    }

    // Read down columns to form each chunk
    const chunks: string[] = [];
    for (let c = 0; c < this.cols; c++) {
      let chunk = '';
      for (let r = 0; r < this.rows; r++) {
        chunk += grid[r][c];
      }
      chunks.push(chunk);
    }

    return chunks.join(' ');
  }

  private normalize(text: string): string {
    // Lowercase and strip non-alphanumeric characters
    return text.toLowerCase().replace(/[^a-z0-9]/g, '');
  }

  private getDimensions(length: number): { rows: number; cols: number } {
    const sqrtLen = Math.sqrt(length);
    let rows = Math.floor(sqrtLen);
    let cols = Math.ceil(sqrtLen);
    // If area is insufficient, increase the row count
    if (rows * cols < length) {
      rows++;
    }
    return { rows, cols };
  }
}
