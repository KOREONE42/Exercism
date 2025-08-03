import math

def cipher_text(plain_text):
    # Step 1: Normalize the text
    normalized = ''.join(c.lower() for c in plain_text if c.isalnum())
    
    if not normalized:
        return ""

    # Step 2: Determine rectangle size
    length = len(normalized)
    r = int(math.floor(math.sqrt(length)))
    c = int(math.ceil(math.sqrt(length)))
    
    if r * c < length:
        r += 1

    # Step 3: Create the grid
    grid = [normalized[i:i+c] for i in range(0, length, c)]

    # Step 4: Read columns to encode
    encoded_chunks = []
    for col in range(c):
        chunk = ''.join(row[col] if col < len(row) else ' ' for row in grid)
        encoded_chunks.append(chunk)
    
    # Step 5: Return result with space-separated chunks
    return ' '.join(encoded_chunks)
