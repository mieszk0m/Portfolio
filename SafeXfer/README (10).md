# SafeXfer — secure file transfer (Client–Server, C)

Minimalistyczny system **bezpiecznej wymiany plików** w architekturze klient–serwer.
Obsługuje **auto-discovery** serwera w LAN (UDP multicast), sesję **TCP** z logowaniem
(**PBKDF2-HMAC-SHA256**) oraz komendy: `ls`, `rm <plik>`, `get <plik>`, `put <plik>`.
Sterowanie i transfer realizowane są jednym połączeniem TCP dzięki prostemu **protokółowi TLV**.

> **Status:** MVP (educational). Brak TLS – do testów w sieci zaufanej/VM.


## ✨ Funkcje
- **Auto-discovery (UDP multicast)**: klient odnajduje serwer w LAN.
- **Sesja TCP (2121)**: logowanie + interaktywny CLI klienta.
- **Operacje na plikach**: `ls`, `rm`, `get`, `put`.
- **Uwierzytelnianie**: PBKDF2-HMAC-SHA256 (100k iter., sól per użytkownik).
- **Protokół TLV (Type–Length–Value)**: sterowanie + transfer w jednym kanale.
- **Walidacja ścieżek**: odrzucanie `..`, `/`, `\` (ochrona przed path traversal).


## 🧱 Struktura repozytorium
```
/safexfer
├─ server/          # serwer: sesje TCP, logowanie, silnik plików, discovery, storage/
├─ client/          # klient CLI: logowanie, pętla komend, discovery probe
├─ common/          # tlv.c/.h (ramki TLV, readn/writen, utils)
└─ Makefile
```

**Moduły:** `SrvCore`, `FileEngine`, `AutoGuard`, `NetDiscovery`, `CLI-Client`.


## 🔌 Protokół i porty
- **Discovery (LAN):** klient wysyła `DISCOVER_SAFEXFER` (UDP multicast) → serwer
  odpowiada `SAFEXFER_SERVER` (unicast z IP/portem).
- **Kanał TCP 2121:** po discovery klient zestawia sesję, loguje się i wydaje komendy.
- **TLV (Type–Length–Value)**  
  - Nagłówek: `1B type`, `2B length (big-endian)`, następnie `value[length]`  
  - Sterujące: `0x01 LOGIN`, `0x02 PASSWORD`, `0x10 OK`, `0x11 ERROR`, `0x20 CMD`, `0x21 TEXT`  
  - Transfer GET: `0x31 FILE_INFO(8B)`, `0x32 FILE_CHUNK`, `0x33 FILE_END`  
  - Transfer PUT: `0x51 PUT_CHUNK`, `0x52 PUT_END`  
  - Domyślny rozmiar value: **4096 B** (łatwy do zwiększania).


## 🛠️ Wymagania
**Linux** (rozwijane i testowane m.in. na Kali/Ubuntu). Wymagane pakiety:
```bash
sudo apt update && sudo apt install -y   build-essential gdb valgrind pkg-config make   libsctp-dev lksctp-tools libssl-dev
```


## ⚙️ Budowanie
```bash
make clean && make
```


## ▶️ Uruchomienie (dwa terminale)
**Terminal 1 – serwer:**
```bash
./server/server
# nasłuch: UDP multicast (discovery), TCP 2121 (sesja)
```

**Terminal 2 – klient:**
```bash
./client/client
# po discovery: logowanie → interaktywny prompt SafeXfer>
```

**Przykład sesji:**
```
Znaleziono serwer SafeXfer pod IP: 192.168.1.18
Login: admin
Hasło: ******
✅ Zalogowano! Komendy: ls | rm <plik> | get <plik> | put <plik> | exit
SafeXfer> put raport.txt
OK
SafeXfer> ls
raport.txt 1024 bytes
SafeXfer> get raport.txt
Pobrano raport.txt (1024/1024)
SafeXfer> rm raport.txt
OK
```


## 👤 Konta i repo serwera
- Format kont: `login:salt_hex:pbkdf2_hex` (plik `server/accounts.txt`).
- Repo plików serwera: `server/storage/` (tworzone automatycznie).


## 🔐 Bezpieczeństwo (MVP)
**Zaimplementowane**
- PBKDF2-HMAC-SHA256 (100k, sól użytkownika).
- Parsowanie binarne TLV (bez evala tekstu).
- Walidacja nazw plików (ochrona przed traversal).

**Ryzyka/Ograniczenia**
- Brak **TLS** (LAN/laby – dane idą jawnie).
- Brak rate-limit/lockout.
- Serwer **jednowątkowy** (blokady przy długich transferach).


## 🧭 Roadmap
- Tryb **demona** + logowanie do **syslog**.
- **Równoległość**: fork/pthreads/epoll.
- **TLS (OpenSSL)** na kanale TCP.
- **SCTP 9899 (multi-stream)** dla wielu plików równolegle.
- **Sumy kontrolne** (SHA-256) po transferze, **rate-limit/lockout**, dziennik audytu.


## 🧪 Testy / debug
- `valgrind` (wycieki), `gdb` (awarie), testy integracyjne CLI (skrypty bash).
- Dla protokołu TLV: testy jednostkowe parsera (`common/tlv.c`).


## 📜 Licencja
Wstaw preferowaną licencję (np. MIT/BSD-2-Clause).
