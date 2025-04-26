# 🧩 GGH Cryptosystem – Symulacja systemu kryptograficznego opartego na kratach

Implementacja kryptosystemu **Goldreich-Goldwasser-Halevi (GGH)**, opartego na problemach z teorii krat (lattices), takich jak **Shortest Vector Problem (SVP)** i **Nearest Vector Problem (NVP)**. GGH to przykład asymetrycznego systemu, który ilustruje mechanizm jednokierunkowej funkcji zapadniowej.  
Projekt powstał w celach edukacyjnych na potrzeby kursu **Kryptografia** na AGH. Szczegóły teoretyczne znajdziesz w `GGH.pdf`.

---

## 📂 Struktura projektu

```
GGH/
├── GGH.pdf               # Teoretyczne wprowadzenie (kratki, SVP, NVP, LLL, ataki)
├── src/
│   ├── generate_keys.py  # Generowanie klucza publicznego i prywatnego
│   ├── encrypt.py        # Szyfrowanie wiadomości (m -> c)
│   ├── decrypt.py        # Deszyfrowanie szyfrogramu (c -> m)
│   ├── keys.json.py      # Przykładowy plik wejściowy z macierzami
│   └── attack_lll.py     # Atak LLL na kryptosystem
├── tests/
│   ├── test_ggh.py       # Testy jednostkowe sprawdzające poprawność algorytmów
│   └── test_lll.py       # Testy jednostkowe sprawdzające skuteczność ataku LLL
└── README.md             # Opis projektu i instrukcja użytkowania

```

---

## ⚙️ Technologie

- **Python 3.8+**
- Biblioteki: `numpy`, `fpylll` (dla algorytmu LLL w testach), `pytest`

Instalacja zależności:
```bash
pip install numpy fpylll pytest
```

---

## 🚀 Instrukcja użytkowania

### 1. Generowanie kluczy

Tworzy **klucz publiczny** (B′) oraz **klucz prywatny** (B, U, B⁻¹, U⁻¹):

```bash
python src/generate_keys.py --dim 4 --out keys.json
```

- `--dim 4` → Wymiar kratki (np. 4×4)  
- `--out keys.json` → Plik wyjściowy z macierzami (format JSON)

---

### 2. Szyfrowanie wiadomości

Przekształca wektor wiadomości `m` (ciąg n liczb całkowitych) do szyfrogramu `c`:

```bash
python src/encrypt.py --keys keys.json --message "4 7 -3 5"
```

- **Wejście:** wektor `m = [4,7,-3,5]`  
- **Wyjście:** szyfrogram `c` oraz użyty wektor błędu `e`

---

### 3. Deszyfrowanie szyfrogramu

Odzyskuje oryginalną wiadomość `m` z szyfrogramu `c`:

```bash
python src/decrypt.py --keys keys.json --ciphertext "[12, 8, 5, 9]"
```

- **Wejście:** szyfrogram `c = [...]`  
- **Wyjście:** oryginalny wektor wiadomości `m`

---

## 🧪 Testy

Aby uruchomić testy sprawdzające poprawność działania algorytmów:

```bash
pytest tests/
```

Testy obejmują generowanie kluczy, poprawność szyfrowania i deszyfrowania.

---

## 📝 Opis plików

- **GGH.pdf** – Szczegółowe wprowadzenie teoretyczne:  
  - Teoria krat, SVP, NVP  
  - Algorytm Babai’ego  
  - Opis ataków (np. LLL)  
  - Przykładowe implementacje  

- **generate_keys.py**  
  - Generuje macierze B (bazowa), U (unimodularna) i B′ = U·B  
  - Zapisuje wszystkie macierze i ich odwrotności w `keys.json`

- **encrypt.py**  
  - Wczytuje klucz publiczny B′  
  - Przekształca wiadomość m na szyfrogram c = m·B′ + e (z losowym błędem e)

- **decrypt.py**  
  - Wykorzystuje B, B⁻¹, U⁻¹ oraz algorytm Babai’ego  
  - Odtwarza oryginalną wiadomość m z szyfrogramu c

- **test_ggh.py**  
  - Zestaw testów do sprawdzenia poprawności generacji kluczy, szyfrowania i deszyfrowania

---

## 📚 Materiały

- `GGH.pdf` – Podstawy teoretyczne, przykłady algorytmów, analiza bezpieczeństwa.  
- Więcej o **lattice-based cryptography**:  
  - [Post-Quantum Cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography)  
  - [Shortest Vector Problem (SVP)](https://en.wikipedia.org/wiki/Shortest_vector_problem)

---

## 👨‍💻 Autorzy

- **Piotr Skoczylas**  
- **Mieszko Makowski**

Projekt na potrzeby kursu **Kryptografia**, AGH, 2024.
