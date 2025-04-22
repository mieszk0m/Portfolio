# 📡 Internal Communication System – Aplikacja Webowa

Projekt aplikacji webowej umożliwiającej **komunikację wewnętrzną** w zespole, zrealizowany z użyciem **HTML**, **Java (Spring Boot)** oraz integracji z usługą mailingową **Postmark**. Projekt powstał w ramach kursu **Zaawansowane Technologie Webowe** na AGH.

**Kod źródłowy nie jest publicznie udostępniony** ze względów bezpieczeństwa. W poniższym README zawarto szczegółowy opis funkcjonalności i architektury systemu.

---

## 🧩 Funkcjonalności systemu

### 📬 Moduł komunikacji (mailing)
- Wysyłanie wiadomości e-mail do użytkowników wewnętrznych.
- Integracja z **Postmark API** do obsługi mailingu transakcyjnego (SMTP + REST).
- Obsługa szablonów e-mail w HTML (responsywne wiadomości).
- System logowania wiadomości (archiwizacja i śledzenie statusów wysyłki).

### 👥 Moduł zarządzania użytkownikami
- Rejestracja i logowanie użytkowników.
- Role i uprawnienia (admin, user).
- Walidacja danych (backend + frontend).

### 📨 Moduł powiadomień
- System powiadomień wewnętrznych w aplikacji (web push).
- Logowanie zdarzeń (np. nowa wiadomość, zmiana statusu konta).

### 🔒 Moduł bezpieczeństwa
- Autoryzacja użytkowników z użyciem **JWT** (JSON Web Tokens).
- Hashowanie haseł (bcrypt).
- Ochrona przed atakami CSRF i XSS (Spring Security).

### 🌐 Interfejs użytkownika (frontend)
- Responsywny interfejs w **HTML + CSS + JavaScript**.
- Dashboard z listą użytkowników, powiadomień i wiadomości.
- Formularze kontaktowe i system zarządzania szablonami wiadomości.

---

## 🏗️ Architektura systemu

```
+-----------------+     REST API     +------------------+      SMTP/REST       +------------+
| Frontend (HTML) |  <----------->  | Backend (Java)   |  <------------->     | Postmark   |
| JS, CSS         |                 | Spring Boot, JWT |                     | (Mailing)  |
+-----------------+                 +------------------+                     +------------+
```

- **Frontend:** klasyczne szablony HTML z JavaScript (bez frameworków SPA).  
- **Backend:** Java Spring Boot, REST API, zabezpieczenia JWT.
- **Mailing:** integracja z Postmark (SMTP + REST API).

---

## 📝 Dokumentacja API

1. **Logowanie użytkownika:**
   ```http
   POST /api/login
   Body: { "username": "admin", "password": "***" }
   Response: { "token": "<JWT>" }
   ```

2. **Wysyłanie wiadomości e-mail:**
   ```http
   POST /api/messages
   Headers: { Authorization: Bearer <JWT> }
   Body: { "to": "user@example.com", "subject": "Subject", "body": "Message content" }
   ```

3. **Pobieranie listy użytkowników:**
   ```http
   GET /api/users
   Headers: { Authorization: Bearer <JWT> }
   ```

---

## 🔧 Wymagania techniczne

- **Java 17**, **Spring Boot 3.x**
- **Maven** (zarządzanie zależnościami)
- **Postmark API Key** (do obsługi mailingu)

---

## 👨‍💻 Autorzy

- **Mieszko Makowski**
- **Karol Mierzwiński**
- **Mateusz Wirkijowski**

Projekt na potrzeby kursu **Zaawansowane Technologie Webowe**, AGH, 2025.

