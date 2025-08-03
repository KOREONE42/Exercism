const complementMap: Record<'G' | 'C' | 'T' | 'A', 'C' | 'G' | 'A' | 'U'> = {
  G: 'C',
  C: 'G',
  T: 'A',
  A: 'U'
};

/**
 * Transcribes a DNA strand into its RNA complement using RNA Interference mapping.
 * @param {string} dna - The DNA sequence to transcribe.
 * @returns {string} - The corresponding RNA sequence.
 * @throws {Error} - If the DNA sequence contains invalid nucleotides.
 */
export function toRna(dna: string): string {
  return dna
    .split('')
    .map((nucleotide: string) => {
      const rna = complementMap[nucleotide as keyof typeof complementMap];
      if (rna === undefined) {
        // Unified error message for any invalid input
        throw new Error('Invalid input DNA.');
      }
      return rna;
    })
    .join('');
}