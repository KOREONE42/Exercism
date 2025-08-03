export class Crypto {
  private normalized: string;
  private encoded: string;

  constructor(plainText: unknown) {
    // Normalize: downcase and remove non-alphanumeric characters
    const text = String(plainText).toLowerCase().replace(/[^a-z0-9]/g, "");
    this.normalized = text;
    this.encoded = this.encode(text);
  }

  get ciphertext(): string {
    return this.encoded;
  }

  private encode(text: string): string {
    const length = text.length;
    if (length === 0) return '';

    // Determine rectangle size
    const sqrt = Math.sqrt(length);
    let rows = Math.floor(sqrt);
    let cols = Math.ceil(sqrt);
    if (rows * cols < length) {
      rows = cols;
    }

    // Break into rows and pad last row if necessary
    const grid: string[] = [];
    for (let i = 0; i < length; i += cols) {
      let row = text.slice(i, i + cols);
      if (row.length < cols) {
        row = row.padEnd(cols, ' ');
      }
      grid.push(row);
    }

    // Read down columns
    const chunks: string[] = [];
    for (let c = 0; c < cols; c++) {
      let chunk = '';
      for (let r = 0; r < rows; r++) {
        const row = grid[r] || ''.padEnd(cols, ' ');
        chunk += row[c] || ' ';
      }
      chunks.push(chunk);
    }

    // Join with spaces
    return chunks.join(' ');
  }
}
