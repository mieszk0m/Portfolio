# 🔐 Portfolio Kryptograficzne

## 📌 Opis
W tym katalogu znajdują się implementacje różnych algorytmów kryptograficznych – zarówno klasycznych, jak i nowoczesnych, w tym systemów podpisów cyfrowych oraz metod analizy tekstu.

---

## 📂 Zawartość
### **🔹 Podpisy cyfrowe**
- **`Drzewo.py`** – Implementacja podpisów Winternitza z drzewem Merkle.
- **`Winternitz.py`** – Implementacja podpisów cyfrowych Winternitza.
- **`lamport.py`** – Implementacja podpisów jednokrotnego użytku Lamporta.

### **🔹 Kryptografia modularna i teoria liczb**
- **`klasaZn.py`** – Arytmetyka modularna w pierścieniach `Zn`.
- **`krypto 10.08.2024.py`** – Znajdowanie pierwiastków pierwotnych i operacje modularne.

### **🔹 Szyfrowanie i ataki na szyfry**
- **`szyfr cezara.py`** – Implementacja klasycznego szyfru Cezara.
- **`szyfr monoalfabetyczny.py`** – Implementacja szyfru monoalfabetycznego z losową permutacją.
- **`ileprobszyfrcezara.py`** – Atak brute-force na szyfr Cezara.
- **`rozkładliterwtekscie.py`** – Analiza częstotliwości liter w tekście (do kryptoanalizy).
- **`rysowaniewykresuczestotliwosci.py`** – Wizualizacja częstości liter w języku angielskim.

### **🔹 Generowanie kluczy kryptograficznych**
- **`kyper.py`** – Implementacja generowania kluczy w systemie kryptograficznym.

---

## 📖 Dokumentacja
📄 **Kryptografia.pdf** – Dokumentacja kryptosystemu GGH i jego matematycznych podstaw.

---

## 🔧 Uruchamianie kodu
Aby uruchomić dowolny plik Python, użyj:
```sh
python3 nazwa_pliku.py
