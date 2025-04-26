# ☁️ Virtualized High-Availability Environment – Projekt Wirtualizacji

Projekt polegający na wdrożeniu zwirtualizowanego środowiska IT o wysokiej dostępności (HA) z wykorzystaniem **VMware vSphere**, **ESXi**, **vCenter Server**, współdzielonej przestrzeni dyskowej **iSCSI** oraz **Windows Server 2016** z usługą **IIS Web Server**. Celem było zapewnienie ciągłości działania usług WWW nawet w przypadku awarii hosta.

---

## 📂 Struktura projektu

```
Virtualization_HA/
├── report.pdf             # Szczegółowy opis projektu (konfiguracja, testy HA)
├── diagrams.png           # Diagram architektury rozwiązania
├── scripts/
│   └── iscsi_setup.ps1    # Skrypty konfiguracji iSCSI (PowerShell)
└── README.md              # Instrukcja i podsumowanie projektu
```

---

## 📝 Opis projektu

- **Technologie:**
  - Hypervisor: VMware ESXi 7.0
  - System zarządzania: VMware vCenter Server
  - Wirtualizacja storage: iSCSI target na VM (Windows Server 2016)
  - System operacyjny VM: Windows Server 2016
  - Usługa: IIS Web Server (port 80)

- **Cele:**
  - Zapewnienie **High Availability (HA)** dla usługi WWW
  - Test migracji maszyn wirtualnych przy awarii hosta
  - Użycie współdzielonej przestrzeni dyskowej (iSCSI)

---

## 🔧 Kluczowe kroki wdrożenia

1. **Instalacja VMware ESXi**
   - Zainstalowano ESXi 7.0 na dwóch hostach (Bay 8, Bay 13).
   - Połączono hosty do lokalnej sieci AGH przez VPN.

2. **Instalacja i konfiguracja vCenter Server**
   - Umożliwiło centralne zarządzanie środowiskiem.

3. **Konfiguracja współdzielonej przestrzeni iSCSI**
   - Dedykowana maszyna wirtualna (Windows Server 2016) jako iSCSI target.
   - Hosty ESXi skonfigurowane do łączenia z iSCSI LUN-ami.

4. **Tworzenie klastra High Availability (HA)**
   - Dodano oba hosty do klastra HA.
   - Skonfigurowano reguły failover (automatyczna migracja VM w razie awarii).

5. **Instalacja maszyn wirtualnych z IIS Web Server**
   - Dwie VM z Windows Server 2016.
   - Zainstalowano i skonfigurowano IIS, testując dostępność strony WWW.

6. **Testowanie failover**
   - Wyłączenie jednego hosta skutkuje automatycznym przeniesieniem VM na drugi.
   - Usługa IIS Web Server działa bez przerwy.

---

## 📊 Diagram architektury

```
+-------------------+           +-------------------+
|    ESXi Host 1    |           |    ESXi Host 2    |
| (Bay 8 - 10.82.x) |           | (Bay 13 - 10.82.x)|
|                   |           |                   |
| +--------------+  |           | +--------------+  |
| | VM: IIS Web  |  |           | | VM: IIS Web  |  |
| +--------------+  |           | +--------------+  |
+---------+---------+           +---------+---------+
          |                               |
          +-------------------------------+
                      |
            +-----------------+
            |  iSCSI Target   |
            | (Windows VM)    |
            +-----------------+
```

---

## 🚀 Wymagania techniczne

- VMware vSphere (ESXi + vCenter Server)
- Windows Server 2016 (dla VM i iSCSI)
- Skonfigurowane połączenia iSCSI
- Dwa fizyczne serwery (Bay 8, Bay 13)

---

## 👨‍💻 Autorzy

- **Mieszko Makowski**
- **Wiktor Deka**
- **Miłosz Gaszyna**
- **Jakub Olech**

Projekt na potrzeby kursu **Wirtualizacja i Bezpieczeństwo IT**, AGH, 2025.

