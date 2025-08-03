import math
import string

ALPHABET_SIZE = 26

def _modinv(a, m):
    """
    Compute the modular inverse of a mod m, i.e. find x such that (a*x) % m == 1.
    Raises ValueError if no inverse exists.
    """
    # Extended Euclidean algorithm
    t0, t1 = 0, 1
    r0, r1 = m, a % m
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    if r0 != 1:
        raise ValueError("a and m must be coprime.")
    return t0 % m

def encode(plain_text, a, b):
    """
    Encrypts plain_text using the affine cipher E(x) = (a*x + b) mod m,
    where x is the 0–25 index of each lowercase letter. Digits are passed through,
    everything else is dropped. Output is lower‑case, grouped in fives.
    """
    # sanity check
    if math.gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError("a and m must be coprime.")

    # build the raw cipher stream (letters → cipher letters, digits → themselves)
    stream = []
    for ch in plain_text:
        if ch.isalpha():
            x = ord(ch.lower()) - ord('a')
            y = (a * x + b) % ALPHABET_SIZE
            stream.append(chr(y + ord('a')))
        elif ch.isdigit():
            stream.append(ch)
        # else: drop spaces/punctuation

    # group into chunks of 5
    groups = [
        ''.join(stream[i:i+5])
        for i in range(0, len(stream), 5)
    ]
    return ' '.join(groups)

def decode(ciphered_text, a, b):
    """
    Decrypts ciphered_text encrypted with E(x) = (a*x + b) mod m
    by computing D(y) = a_inv * (y - b) mod m. Letters only; digits pass through.
    All spaces/punctuation are dropped and output is one continuous string.
    """
    # sanity check
    if math.gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError("a and m must be coprime.")

    a_inv = _modinv(a, ALPHABET_SIZE)

    plain = []
    for ch in ciphered_text:
        if ch.isalpha():
            y = ord(ch.lower()) - ord('a')
            x = (a_inv * (y - b)) % ALPHABET_SIZE
            plain.append(chr(x + ord('a')))
        elif ch.isdigit():
            plain.append(ch)
        # else: drop spaces/punctuation

    return ''.join(plain)
