from __future__ import annotations
from typing import List

# -----------------------------------------------------------------------------
#  0. Struktury trytowe (MSB‑first)
# -----------------------------------------------------------------------------
class Tryt(int):
    __slots__ = ()
    def __new__(cls, v: int) -> "Tryt":
        return int.__new__(cls, v % 3)
    def __xor__(self, o: int) -> "Tryt":
        return Tryt((int(self) + int(o)) % 3)
    def __and__(self, o: int) -> "Tryt":
        return Tryt(min(int(self), int(o)))
    def __or__(self, o: int) -> "Tryt":
        return Tryt(max(int(self), int(o)))
    def __invert__(self) -> "Tryt":
        return Tryt(2 - int(self))

class TrytSeq(List[Tryt]):
    def rot(self, n: int) -> "TrytSeq":
        n %= len(self)
        return TrytSeq(self[n:] + self[:n])
    def __xor__(self, other: "TrytSeq") -> "TrytSeq":
        return TrytSeq([t ^ other[i] for i, t in enumerate(self)])
    __rxor__ = __xor__
    def __and__(self, other: "TrytSeq") -> "TrytSeq":
        return TrytSeq([t & other[i] for i, t in enumerate(self)])
    def __or__(self, other: "TrytSeq") -> "TrytSeq":
        return TrytSeq([t | other[i] for i, t in enumerate(self)])
    def __invert__(self) -> "TrytSeq":
        return TrytSeq([~t for t in self])
    @staticmethod
    def from_int(val: int, length: int) -> "TrytSeq":
        tr: List[Tryt] = []
        v = val
        while v:
            tr.append(Tryt(v % 3))
            v //= 3
        tr = tr[::-1]
        if len(tr) < length:
            tr = [Tryt(0)] * (length - len(tr)) + tr
        else:
            tr = tr[-length:]
        return TrytSeq(tr)
    @staticmethod
    def from_bytes(data: bytes) -> "TrytSeq":
        out: List[Tryt] = []
        for b in data:
            out.extend(TrytSeq.from_int(b, 6))
        return TrytSeq(out)

_clone = lambda ts: TrytSeq(ts)
_add   = lambda a,b: TrytSeq([(a[i] + b[i]) for i in range(len(a))])

# -----------------------------------------------------------------------------
#  1. Ternarny SHA‑256  (168 trytów)
# -----------------------------------------------------------------------------
WORD_LEN = 21
BLOCK_WORDS = 16
ROUNDS = 64
IV_INT = [
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19,
]
IV = [TrytSeq.from_int(v, WORD_LEN) for v in IV_INT]

_sigma0  = lambda w: w.rot(1) ^ w.rot(5)  ^ w.rot(10)
_sigma1  = lambda w: w.rot(2) ^ w.rot(7)  ^ w.rot(15)
_Sigma0  = lambda w: w.rot(3) ^ w.rot(9)  ^ w.rot(14)
_Sigma1  = lambda w: w.rot(6) ^ w.rot(11) ^ w.rot(17)

# padding trytów
def _pad(ts: TrytSeq) -> TrytSeq:
    L = len(ts)
    ts.append(Tryt(1))
    while (len(ts) + WORD_LEN) % (BLOCK_WORDS * WORD_LEN):
        ts.append(Tryt(0))
    ts.extend(TrytSeq.from_int(L, WORD_LEN))
    return ts

def sha256_trit(data: bytes) -> TrytSeq:
    msg = _pad(TrytSeq.from_bytes(data))
    H = [_clone(w) for w in IV]
    for off in range(0, len(msg), WORD_LEN * BLOCK_WORDS):
        blk = msg[off : off + WORD_LEN * BLOCK_WORDS]
        W = [TrytSeq(blk[i*WORD_LEN:(i+1)*WORD_LEN]) for i in range(BLOCK_WORDS)]
        for t in range(16, ROUNDS):
            W.append(_add(_add(_sigma1(W[t-2]), W[t-7]), _add(_sigma0(W[t-15]), W[t-16])))
        a,b,c,d,e,f,g,h = (_clone(w) for w in H)
        for t in range(ROUNDS):
            t1 = _add(h, _add(_Sigma1(e), _add((e & f) | (~e & g), W[t])))  # pominięto stałe K
            t2 = _add(_Sigma0(a), (a & b) | (a & c) | (b & c))
            h,g,f,e,d,c,b,a = g,f,e,_add(d,t1),c,b,a,_add(t1,t2)
        H = [_add(x,y) for x,y in zip(H,[a,b,c,d,e,f,g,h])]
    return TrytSeq([t for w in H for t in w])

# -----------------------------------------------------------------------------
#  2. Test jednostkowy
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    out = sha256_trit(b"abc")
    assert len(out) == 168, "Skrót powinien mieć dokładnie 168 trytów"
    print("SHA‑256 trit len:", len(out))
    print("Pierwsze 15 trytów:",[int(t) for t in out][:15])
    print("✓ Ternarny SHA‑256 przechodzi test długości")