SafeXfer — secure file transfer (Client–Server, C)

Minimalistyczny system bezpiecznej wymiany plików w architekturze klient–serwer.
Obsługuje auto-discovery serwera w LAN (UDP multicast), sesję TCP z logowaniem (PBKDF2-HMAC-SHA256) oraz polecenia: ls, rm <plik>, get <plik>, put <plik>. Sterowanie i transfer w jednym kanale TCP dzięki prostemu protokółowi TLV.

✨ Funkcje (MVP)

Auto-discovery (UDP multicast): 224.0.0.251:54321

Sesja TCP (domyślnie port 2121): logowanie + interaktywny CLI

Operacje na plikach: ls, rm, get, put

Uwierzytelnianie: PBKDF2-HMAC-SHA256 (100k iteracji, sól per użytkownik)

Protokół TLV: sterowanie + transfer w jednym połączeniu TCP

Bezpieczeństwo ścieżek: odrzucanie .., /, \ (ochrona przed path traversal)

🧱 Architektura i repo
/safexfer
├─ server/         # main.c, SrvCore (sesje TCP + FileEngine), AutoGuard, NetDiscovery, storage/
├─ client/         # main.c, CLI (logowanie + pętla komend), NetDiscovery probe
├─ common/         # tlv.c/.h (ramki TLV, readn/writen)
└─ Makefile


Moduły: SrvCore, FileEngine, AutoGuard, NetDiscovery, CLI-Client.

🔌 Protokół i porty

Discovery: klient wysyła DISCOVER_SAFEXFER → serwer odpowiada SAFEXFER_SERVER (unicast)

Kanał TCP 2121: po discovery klient zestawia sesję, loguje się i wydaje komendy

TLV (Type-Length-Value)

Nagłówek: 1B type, 2B length (BE), następnie value[length]

Sterujące: 0x01 LOGIN, 0x02 PASSWORD, 0x10 OK, 0x11 ERROR, 0x20 CMD, 0x21 TEXT

Transfer GET: 0x31 FILE_INFO(8B), 0x32 FILE_CHUNK, 0x33 FILE_END

Transfer PUT: 0x51 PUT_CHUNK, 0x52 PUT_END

Domyślny rozmiar value: 4096 B (łatwy do zwiększania)

🛠️ Wymagania i budowanie

Linux (rozwijane na Kali). Wymagane pakiety:

sudo apt update && sudo apt install -y \
  build-essential gdb valgrind pkg-config make \
  libsctp-dev lksctp-tools libssl-dev


Budowanie:

make clean && make


Uruchomienie – 2 terminale:

# Terminal 1 – serwer:
./server/server
# nasłuch: UDP 224.0.0.251:54321 (discovery), TCP 2121 (sesja)

# Terminal 2 – klient:
./client/client
# po discovery: login/hasło → interaktywny prompt SafeXfer>


Przykładowa sesja:

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


🔐 Bezpieczeństwo (stan MVP)

Zaimplementowane

PBKDF2-HMAC-SHA256 (100k, sól per user)

Parsowanie TLV (binarnie; brak evala tekstu)

Walidacja nazw plików (ochrona przed traversal)

Ryzyka/ograniczenia

Brak TLS (LAN/laby – dane idą jawnie)

Brak rate-limit/lockout

Serwer jednowątkowy (blokuje się przy długich transferach)

🧭 Roadmap (prace dalsze)

Tryb demona + logowanie do syslog

Równoległość: fork/pthreads/epoll

TLS (OpenSSL) dla kanału TCP

SCTP 9899 (multi-stream) dla równoległego transferu wielu plików

Sumy kontrolne (SHA-256) po transferze, rate-limit/lockout, dziennik audytu


📋 Konta i repozytorium plików

Format kont: login:salt_hex:pbkdf2_hex (plik server/accounts.txt)

Repo plików serwera: server/storage/ (tworzone automatycznie)

⚖️ Licencja

Wstaw preferowaną licencję (np. MIT/BSD-2-Clause).
