# 🔐 Analiza Porównawcza Mechanizmów Uwierzytelniania

Kompleksowa analiza bezpieczeństwa, funkcjonalności oraz kosztów wdrożenia sześciu najpopularniejszych mechanizmów uwierzytelniania stosowanych w transakcjach elektronicznych oraz ochronie kont użytkowników. Projekt powstał w ramach kursu **Bezpieczne Transakcje Elektroniczne** na AGH.

---

## 📂 Struktura projektu

```
Authentication_Analysis/
├── Authentication_Mechanisms_Analysis.pdf  # Pełny raport analizy porównawczej
├── presentation/                           # Folder z prezentacją podsumowującą
│   └── slides.pdf                          # Slajdy prezentacji projektu
└── README.md                               # Opis projektu i podsumowanie analizy
```

---

## 📝 Zakres analizy

### Porównywane mechanizmy uwierzytelniania:
1. **Hasła klasyczne**
2. **Dwuskładnikowa autoryzacja (2FA)**
3. **Klucze sprzętowe (np. FIDO)**
4. **Biometria**
5. **Single Sign-On (SSO)**
6. **OAuth2/JWT**

### Kryteria oceny:
- **Uniwersalność zastosowania**
- **Funkcjonalność dla użytkownika końcowego**
- **Odporność na ataki**
- **Aspekty bezpieczeństwa (poufność, integralność)**
- **Inne aspekty techniczne i koszty wdrożenia**

---

## 🚀 Kluczowe wnioski z analizy

### 1. **Najwyższa odporność na ataki**:
- **Klucze sprzętowe (FIDO)** i **Biometria**
  - Oparte na fizycznych nośnikach i unikalnych cechach użytkownika.
  - Skutecznie chronią przed phishingiem i przejęciem danych.

### 2. **Największa funkcjonalność i wygoda**:
- **Single Sign-On (SSO)**, **Biometria**, **OAuth2/JWT**
  - Wysoki komfort użytkownika (jednokrotne logowanie, brak potrzeby pamiętania haseł).

### 3. **Najniższe koszty wdrożenia**:
- **Hasła klasyczne**
  - Brak konieczności dodatkowego sprzętu.

- **OAuth2/JWT**
  - Brak licencji, jedynie koszt wdrożenia programistycznego.

### 4. **Najwyższe koszty wdrożenia**:
- **Biometria**
  - Potrzeba specjalistycznego sprzętu (np. skanery tęczówki, odcisków palców).

---

## 📊 Przykładowe zastosowania

- **Hasła klasyczne:** logowanie do e-maili, portali społecznościowych, systemów operacyjnych.
- **2FA:** bankowość internetowa, chmura, gry online.
- **Klucze sprzętowe:** VPN, konta programistyczne (GitHub), logowanie do korporacyjnych systemów.
- **Biometria:** smartfony, płatności mobilne, systemy medyczne.
- **SSO:** korporacyjne platformy (Slack, ERP, CRM).
- **OAuth2/JWT:** autoryzacja w aplikacjach webowych i API (np. „Zaloguj się przez Google”).

---

## 🧩 Użyte narzędzia i źródła

- Narzędzia do współpracy: **Discord** (komunikacja zespołowa).
- Raporty i dokumentacja: zawarte w pliku `Authentication_Mechanisms_Analysis.pdf`.
- Bibliografia (m.in.): Wikipedia, Microsoft, Auth0, Norton, ScienceDirect.

---

## 👨‍💻 Autorzy

- **Mateusz Wirkijowski**
- **Mieszko Makowski**
- **Bartosz Grzybowski**
- **Patryk Motylski**
- **Dawid Ryba**
- **Mikołaj Pacek**

Projekt na potrzeby kursu **Bezpieczne Transakcje Elektroniczne**, AGH, 2025.

