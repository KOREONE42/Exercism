def proteins(strand):
    """
    Translates an RNA sequence into a list of protein names (amino acids) based on codons.

    Parameters:
        strand (str): A string representing the RNA sequence (e.g., "AUGUUUUCU").

    Returns:
        List[str]: A list of protein names (e.g., ["Methionine", "Phenylalanine", "Serine"]).
                   Translation stops at a STOP codon if encountered.
    """
    
    # Dictionary mapping codons to their corresponding amino acids
    codon_table = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine", "UUG": "Leucine",
        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
        "UAU": "Tyrosine", "UAC": "Tyrosine",
        "UGU": "Cysteine", "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }

    protein_sequence = []  # List to store resulting protein names

    # Process RNA strand in steps of 3 (codon length)
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]

        # Stop translation if a STOP codon is found
        if codon_table.get(codon) == "STOP":
            break

        # Append corresponding amino acid if valid codon
        amino_acid = codon_table.get(codon)
        if amino_acid:
            protein_sequence.append(amino_acid)

    return protein_sequence
