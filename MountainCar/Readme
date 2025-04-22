# 🚗 Mountain Car Simulation – Modelowanie fizyki pojazdu w dolinie

Symulacja klasycznego problemu **Mountain Car** w środowisku OpenAI Gym. Celem jest zademonstrowanie działania modelu fizycznego pojazdu poruszającego się w dolinie, wykorzystując prosty algorytm sterowania ruchem. Projekt powstał na potrzeby kursu **Sztuczna Inteligencja** na AGH.

---

## 📂 Struktura projektu

```
MountainCar/
├── src/
│   └── mountain_car.py     # Kod symulacji i wizualizacji
├── data/
│   └── results.png         # Przykładowe wykresy wyników symulacji
└── README.md               # Instrukcja i opis projektu
```

---

## ⚙️ Technologie

- **Python 3.8+**
- Biblioteki: `gym`, `matplotlib`, `numpy`

Instalacja zależności:
```bash
pip install gym matplotlib numpy
```

---

## 📖 Opis modelu fizycznego

- **Zakres pozycji:** `[-1.2, 0.6]`
- **Zakres prędkości:** `[-0.07, 0.07]`
- **Siła napędu:** `0.001`
- **Grawitacja:** `0.0025`
- **Trzy możliwe akcje:**
  - `0` – przyspieszenie w lewo
  - `1` – brak przyspieszenia
  - `2` – przyspieszenie w prawo
- Zderzenia na obu końcach są niesprężyste – po kolizji prędkość ustawiana jest na `0`.

Aktualizacja stanu pojazdu:
```
przyspieszenie(t+1) = przyspieszenie(t) + (akcja - 1) * siła - grawitacja * cos(3 * pozycja(t))
pozycja(t+1) = pozycja(t) + przyspieszenie(t+1)
```

---

## 🚀 Instrukcja uruchomienia

1. Przejdź do folderu projektu:
```bash
cd MountainCar
```
2. Uruchom symulację:
```bash
python src/mountain_car.py --episodes 1000 --render
```
- `--episodes 1000` – liczba epizodów symulacji
- `--render` – wyświetlanie animacji środowiska

---

## 📊 Wyniki

- Przykładowe wykresy wyników (np. osiągnięta pozycja, przyspieszenie w czasie) znajdują się w folderze `data/results.png`.
- Analiza danych opiera się na liczbie kroków potrzebnych do osiągnięcia celu oraz wizualizacji trajektorii.

---

## 👨‍💻 Autorzy

- **Mieszko Makowski**
- **Dawid Ryba**

Projekt na potrzeby kursu **Sztuczna Inteligencja**, AGH, 2024.
