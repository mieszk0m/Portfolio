from __future__ import annotations
from typing import List

# -----------------------------------------------------------------------------
#  Sekcja 0 – Operacje binarne (32 bit)
# -----------------------------------------------------------------------------
MASK_32 = 0xFFFFFFFF

def rotl32(x: int, n: int) -> int:
    n &= 31
    return ((x << n) | (x >> (32 - n))) & MASK_32

def shr32(x: int, n: int) -> int:
    return (x >> n) & MASK_32

bit_and = lambda a, b: a & b
bit_or  = lambda a, b: a | b
bit_xor = lambda a, b: a ^ b
bit_not = lambda a: (~a) & MASK_32

# -----------------------------------------------------------------------------
#  Sekcja 1 – Implementacja SHA‑1 (binarna)
# -----------------------------------------------------------------------------

def _preprocess(data: bytes) -> List[int]:
    #Zamienia bajty na listę 32‑bitowych słów (big‑endian) po paddingu
    bit_len = len(data) * 8
    data += b"\x80"                     # dodaj 1‑bit (0x80)
    while (len(data) % 64) != 56:        # dopełnij zerami do 56 mod 64
        data += b"\x00"
    data += bit_len.to_bytes(8, "big")   # 64‑bitowa długość

    words: List[int] = []
    for i in range(0, len(data), 4):
        words.append(int.from_bytes(data[i:i+4], "big"))
    return words


def sha1(data: bytes) -> str:
    """Zwraca 40‑znakowy heksadecymalny skrót SHA‑1 wejścia `data`."""
    h0, h1, h2, h3, h4 = (
        0x67452301, 0xEFCDAB89, 0x98BADCFE,
        0x10325476, 0xC3D2E1F0,
    )

    words = _preprocess(data)

    for offset in range(0, len(words), 16):
        w = words[offset : offset + 16] + [0] * 64
        for t in range(16, 80):
            w[t] = rotl32(w[t - 3] ^ w[t - 8] ^ w[t - 14] ^ w[t - 16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for t in range(80):
            if t < 20:
                f, k = (b & c) | ((~b) & d), 0x5A827999
            elif t < 40:
                f, k = b ^ c ^ d, 0x6ED9EBA1
            elif t < 60:
                f, k = (b & c) | (b & d) | (c & d), 0x8F1BBCDC
            else:
                f, k = b ^ c ^ d, 0xCA62C1D6

            temp = (rotl32(a, 5) + f + e + k + w[t]) & MASK_32
            e, d, c, b, a = d, c, rotl32(b, 30), a, temp

        h0 = (h0 + a) & MASK_32
        h1 = (h1 + b) & MASK_32
        h2 = (h2 + c) & MASK_32
        h3 = (h3 + d) & MASK_32
        h4 = (h4 + e) & MASK_32

    return "".join(f"{x:08x}" for x in (h0, h1, h2, h3, h4))

# -----------------------------------------------------------------------------
#  Testy / demonstracja
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test RFC 3174
    assert sha1(b"abc") == "a9993e364706816aba3e25717850c26c9cd0d89d"
    print("SHA‑1(abc) → OK")

    # Własna wiadomość – używamy ASCII‑hyphena, aby uniknąć błędu bytes‑literal
    msg = b"Egzamin na 3"
    print("\nWiadomość:", msg)
    print("SHA‑1     :", sha1(msg))

    # Krótki dodatkowy test – hash pustego ciągu (sprawdzany z dokumentacji)
    assert sha1(b"") == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    print("SHA‑1("") → OK")

    print("\nEtap 2 ukończony ✔️ – implementacja SHA‑1 (binarnie) przechodzi testy.")
