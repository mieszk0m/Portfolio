
from __future__ import annotations
from typing import List

# -----------------------------------------------------------------------------
#  Sekcja 0 – Operacje binarne (32 bit)
# -----------------------------------------------------------------------------
MASK_32 = 0xFFFFFFFF

def rotl32(x: int, n: int) -> int:
    n &= 31
    return ((x << n) | (x >> (32 - n))) & MASK_32

def rotr32(x: int, n: int) -> int:
    n &= 31
    return ((x >> n) | (x << (32 - n))) & MASK_32

def shr32(x: int, n: int) -> int:
    return (x >> n) & MASK_32


# -----------------------------------------------------------------------------
#  Sekcja 1 – SHA‑256 (binarnie)
# -----------------------------------------------------------------------------
K256 = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
]

def _preprocess_sha256(data: bytes) -> List[int]:
    bit_len = len(data)*8
    data += b"\x80"
    while (len(data)%64)!=56:
        data += b"\x00"
    data += bit_len.to_bytes(8,"big")
    return [int.from_bytes(data[i:i+4],"big") for i in range(0,len(data),4)]


def _sigma0(x:int)->int: return rotr32(x,7)^rotr32(x,18)^shr32(x,3)

def _sigma1(x:int)->int: return rotr32(x,17)^rotr32(x,19)^shr32(x,10)

def _Sigma0(x:int)->int: return rotr32(x,2)^rotr32(x,13)^rotr32(x,22)

def _Sigma1(x:int)->int: return rotr32(x,6)^rotr32(x,11)^rotr32(x,25)

def sha256(data: bytes) -> str:
    a,b,c,d,e,f,g,h = (
        0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
        0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19,
    )
    words=_preprocess_sha256(data)
    for off in range(0,len(words),16):
        w=words[off:off+16]+[0]*48
        for t in range(16,64):
            w[t]=(w[t-16]+_sigma0(w[t-15])+w[t-7]+_sigma1(w[t-2]))&MASK_32
        A,B,C,D,E,F,G,H=a,b,c,d,e,f,g,h
        for t in range(64):
            t1=(H+_Sigma1(E)+((E & F)^((~E)&G))+K256[t]+w[t])&MASK_32
            t2=(_Sigma0(A)+((A & B)^(A & C)^(B & C)))&MASK_32
            H=G; G=F; F=E; E=(D+t1)&MASK_32
            D=C; C=B; B=A; A=(t1+t2)&MASK_32
        a=(a+A)&MASK_32; b=(b+B)&MASK_32; c=(c+C)&MASK_32; d=(d+D)&MASK_32
        e=(e+E)&MASK_32; f=(f+F)&MASK_32; g=(g+G)&MASK_32; h=(h+H)&MASK_32
    return "".join(f"{x:08x}" for x in (a,b,c,d,e,f,g,h))

# -----------------------------------------------------------------------------
#  Testy / demonstracja
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # === SHA‑1 testy ===
    assert sha1(b"abc") == "a9993e364706816aba3e25717850c26c9cd0d89d"
    assert sha1(b"")   == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    print("SHA‑1 tests OK")

    # === SHA‑256 testy ===
    assert sha256(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert sha256(b"")   == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    print("SHA‑256 tests OK")

    msg = b"Hello SHA-256!"
    print("\nWiadomość:", msg)
    print("SHA‑256  :", sha256(msg))
    print("\nEtap 3 ukończony ✔️ – SHA‑256 (binarnie) działa i przechodzi testy.")
