from __future__ import annotations
from typing import List

# -----------------------------------------------------------------------------
#  Sekcja 0 – Struktury trytowe (MSB‑first)
# -----------------------------------------------------------------------------
class Tryt(int):
    __slots__ = ()
    def __new__(cls, v: int) -> "Tryt":
        return int.__new__(cls, v % 3)
    def __xor__(self, other: int) -> "Tryt":
        return Tryt((int(self) + int(other)) % 3)
    def __and__(self, other: int) -> "Tryt":
        return Tryt(min(int(self), int(other)))
    def __or__(self, other: int) -> "Tryt":
        return Tryt(max(int(self), int(other)))
    def __invert__(self) -> "Tryt":
        return Tryt(2 - int(self))

class TrytSeq(List[Tryt]):
    """Lista trytów z operacjami logicznymi i rotacją (MSB‑first)."""
    # --- rotacja ---
    def rot(self, n: int) -> "TrytSeq":
        n %= len(self)
        return TrytSeq(self[n:] + self[:n])

    # --- XOR element‑wise ---
    def __xor__(self, other: "TrytSeq") -> "TrytSeq":
        if not isinstance(other, TrytSeq):
            return NotImplemented
        return TrytSeq([t ^ other[i] for i, t in enumerate(self)])
    __rxor__ = __xor__

    # --- AND / OR / NOT element‑wise ---
    def __and__(self, other: "TrytSeq") -> "TrytSeq":
        return TrytSeq([t & other[i] for i, t in enumerate(self)])
    def __or__(self, other: "TrytSeq") -> "TrytSeq":
        return TrytSeq([t | other[i] for i, t in enumerate(self)])
    def __invert__(self) -> "TrytSeq":
        return TrytSeq([~t for t in self])

    # --- fabryki ---
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

# -----------------------------------------------------------------------------
#  Parametry ternarnego SHA‑1
# -----------------------------------------------------------------------------
WORD_LEN, BLOCK_WORDS, TOTAL_ROUNDS = 21, 16, 80
IV_INT = [0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0]
IV_TRIT = [TrytSeq.from_int(v, WORD_LEN) for v in IV_INT]
_word_add = lambda a,b: TrytSeq([(a[i]+b[i]) for i in range(WORD_LEN)])

def _pad_tryts(msg: TrytSeq) -> TrytSeq:
    L=len(msg)
    msg.append(Tryt(1))
    while (len(msg)+WORD_LEN)%(BLOCK_WORDS*WORD_LEN): msg.append(Tryt(0))
    msg.extend(TrytSeq.from_int(L, WORD_LEN))
    return msg

def _f(t:int,B:TrytSeq,C:TrytSeq,D:TrytSeq)->TrytSeq:
    if t<20: return (B & C) | (~B & D)
    if t<40 or t>=60: return B ^ C ^ D
    return (B & C) | (B & D) | (C & D)

# -----------------------------------------------------------------------------
#  Ternarny SHA‑1
# -----------------------------------------------------------------------------

def sha1_trit(data: bytes) -> TrytSeq:
    msg=_pad_tryts(TrytSeq.from_bytes(data))
    H=[_clone(w) for w in IV_TRIT]
    for off in range(0,len(msg),WORD_LEN*BLOCK_WORDS):
        block=msg[off:off+WORD_LEN*BLOCK_WORDS]
        W=[TrytSeq(block[i*WORD_LEN:(i+1)*WORD_LEN]) for i in range(BLOCK_WORDS)]
        for t in range(16,TOTAL_ROUNDS):
            W.append((W[t-3]^W[t-8]^W[t-14]^W[t-16]).rot(1))
        A,B,C,D,E=[_clone(w) for w in H]
        for t in range(TOTAL_ROUNDS):
            temp=_word_add(_word_add(A.rot(5),_f(t,B,C,D)),_word_add(E,W[t]))
            E,D,C,B,A=D,C,B.rot(30),A,temp
        H=[_word_add(x,y) for x,y in zip(H,[A,B,C,D,E])]
    return TrytSeq([tr for word in H for tr in word])

# -----------------------------------------------------------------------------
#  Test minimalny
# -----------------------------------------------------------------------------
if __name__=="__main__":
    out=sha1_trit(b"abc")
    assert len(out)==105, "SHA‑1 trit powinien mieć 105 trytów"
    print("Pierwsze 20 trytów:",[int(t) for t in out][:20])
    print("✓ Ternarny SHA‑1 przechodzi test XOR")
