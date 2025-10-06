# Ternary Hash — SHA‑1 & SHA‑256 (binary) + ternary variants

Implementacja **SHA‑1** i **SHA‑256** w Pythonie (warianty binarne), wraz z badawczymi
odpowiednikami **ternarnymi** (operującymi na *trytach* zamiast bitów). Projekt służy celom
edukacyjnym i porównawczym (długość skrótu, operatory, padding, rotacje).

> **Status:** PoC/edu. Ternarne wersje są koncepcyjne (nie zapewniają właściwości kryptograficznych
> oryginałów; brak stałych `K` w SHA‑256‑trit i inne uproszczenia).

---

## 📂 Struktura repozytorium

```
/ternary-hash
├─ sha1.py          # klasyczny SHA‑1 (bity) + testy wektorów RFC
├─ sha256.py        # klasyczny SHA‑256 (bity) + testy wektorów
├─ tryt_sha1.py     # SHA‑1 (ternarny) – struktury Tryt/TrytSeq, padding, rundy
├─ tryt_sha256.py   # SHA‑256 (ternarny) – Tryt/TrytSeq, funkcje sigm, kompresja
└─ README.md
```

**Dowody w kodzie:**  
- `sha1.py` zawiera preprocess (padding 0x80 → 56 mod 64 → długość 64‑bit), rundy 0..79
  i testy m.in. `abc`/pusty ciąg. fileciteturn15file0  
- `sha256.py` definiuje tablicę **K256** i przechodzi testy `abc`/pusty; pokazano
  funkcje Σ/σ i pętlę kompresji 64‑rundową. fileciteturn15file1  
- `tryt_sha1.py` wprowadza typy **Tryt/TrytSeq**, padding trytowy (długość w 21‑trytowym słowie),
  f‑funkcje rund i asercję, że wynik ma **105 trytów**. fileciteturn15file2  
- `tryt_sha256.py` rozszerza model na **SHA‑256‑trit** (168 trytów), rotacje/Σ/σ na trytach
  i kompresję bez stałych `K` (uproszczenie do eksperymentów). fileciteturn15file3

---

## 🚀 Szybki start

Wymaga **Python 3.10+**.

```bash
# (opcjonalnie) python -m venv .venv && source .venv/bin/activate
python sha1.py        # uruchamia testy SHA‑1
python sha256.py      # uruchamia testy SHA‑256
python tryt_sha1.py   # test długości ternarnego SHA‑1 (105 trytów)
python tryt_sha256.py # test długości ternarnego SHA‑256 (168 trytów)
```

Użycie w kodzie:

```python
from sha1 import sha1
from sha256 import sha256
from tryt_sha1 import sha1_trit
from tryt_sha256 import sha256_trit

msg = b"abc"
print(sha1(msg))            # 40‑znakowy hex
print(sha256(msg))          # 64‑znakowy hex
t1 = sha1_trit(msg)         # lista 105 trytów (0..2)
t2 = sha256_trit(msg)       # lista 168 trytów (0..2)
```

---

## 🧠 Założenia i różnice (ternary vs binary)

- **Nośnik informacji:** bity → *tryty* (`0,1,2`) reprezentowane klasami `Tryt`/`TrytSeq` z
  operatorami XOR/AND/OR/NOT i rotacją (MSB‑first). fileciteturn15file2  
- **Padding:** analog binarnego – dopełnienie `1` + `0` do granicy bloku i dołączenie długości
  w **21‑trytowym słowie** (odwzorowanie długości wiadomości). fileciteturn15file2  
- **Funkcje rund:** trytowe odpowiedniki `f` (20/40/60/80) i Σ/σ zrealizowane rotacjami sekwencji
  trytów. fileciteturn15file2turn15file3  
- **Uproszczenia bezpieczeństwa:** brak stałych `K` w SHA‑256‑trit; działania na trytach są addytywne
  modulo 3 i nie mają dowiedzionych własności krypto porównywalnych z binarnymi SHA. fileciteturn15file3

---

## 🧪 Testy

Każdy moduł posiada prosty blok `if __name__ == "__main__":` z asercjami:  
- `sha1.py`: porównanie z wektorami `abc` i pustego ciągu. fileciteturn15file0  
- `sha256.py`: porównanie z wektorami `abc` i pustego ciągu. fileciteturn15file1  
- `tryt_sha1.py`: asercja długości 105 trytów + podgląd prefiksu. fileciteturn15file2  
- `tryt_sha256.py`: asercja długości 168 trytów + prefiks. fileciteturn15file3

---

## ⚠️ Zastrzeżenia

- Implementacje **ternarne** są **eksperymentalne** i nie powinny być traktowane jako bezpieczne
  prymitywy krypto w środowiskach produkcyjnych. fileciteturn15file3  
- Celem projektu jest **nauka**: struktury danych, padding, harmonogram słów, rotacje i wpływ
  nośnika informacji (bit vs tryt) na budowę funkcji skrótu.

---

## 🗺️ Roadmap

- Stałe rund (`K`) dla modelu ternarnego SHA‑256 i analiza ich wpływu. fileciteturn15file3  
- Więcej testów właściwości (dyfuzja, zmiana jednego trytu).  
- Eksport/serializacja skrótu ternarnego (np. do zapisu w base‑3 / base‑9).

---

## 📜 Licencja

Wstaw wybraną licencję (np. MIT/BSD‑2‑Clause).
