# Medikamenten-Check
💊 Vault-Tec™ Medikamenten-Check  

# 💊 Vault-Tec™ Medikamenten-Check  
### (Health Monitoring Assistant v1.0)

> *„Mentats vergessen? Kein Problem – dein Pip-Boy erinnert dich.“*  

Dieses Fallout-inspirierte Python-Tool unterstützt dich bei der **Kontrolle und Erinnerung an Medikamenteneinnahmen**.  
Ideal für Vault-Überlebende, Wasteland-Medics oder den Alltag im Büro-Ödland.  

---

## 🎮 Features

- **Patientendaten abfragen**  
  - Name  
  - Geburtsdatum  
  - Diagnosen  

- **Medikamentenverwaltung**  
  - Eingabe von beliebig vielen Medikamenten  
  - Geplante Einnahmezeit hinterlegen  
  - Abfragen, ob das Medikament bereits genommen wurde  

- **Vault-Tec™ Konsolenanzeige**  
  - ✅ Grün = Medikament genommen  
  - ⚠️ Gelb = Einnahmezeit erreicht → Erinnerung!  
  - ⏳ Neutral = Einnahme liegt noch in der Zukunft  
  - ❌ Rot = Übersicht aller noch offenen Medikamente  

---

## ⚙️ Installation

1. Klone das Repo oder kopiere die Datei:  
   ```bash
   git clone https://github.com/NarunaOdinsdottir/medicheck.git
   cd medicheck
2. Starte das Programm :
   python medicheck.py
3. Folge den Anweisungen und erhalte eine farbige Übersicht der Medikamenteneinnahme

## 🖥️ Beispielausgabe

--- Patientendaten ---
Name: Sarah Connor
Geburtsdatum: 13.05.1975
Diagnose(n): Chronische Schmerzen

--- Checkliste Medikamenteneinnahme ---
Ibu 600 ist für später geplant (20:00).
Tavor wurde bereits genommen.
Paracetamol sollte um 10:00 genommen werden!

Noch einzunehmende Medikamente heute:
- Paracetamol um 10:00

## 🏆 Roadmap (Vault-Tec Approved)

-Speicherung der Medikationspläne (JSON/SQLite)
-Automatische Erinnerungen per Notification/Sound
-GUI im Pip-Boy Look mit Statusanzeigen
-Integration in das Vault-Tec Self-Care Terminal

## 🧪 Status

Stable – Einsatzbereit für den medizinischen Alltag.
Vault-Tec übernimmt keine Haftung bei mutierten Nebenwirkungen.

## 📜 Lizenz

Vault-Tec Medical License v2077
„Because selbst im Ödland darfst du keine Tablette vergessen.“


### Weiterentwicklung zu VaultMed ###

## 💊 1. Von Liste → SQL-Datenbank (lokal, sicher)
  
SQLite ist leichtgewichtig, läuft offline, und macht deine Daten strukturiert und erweiterbar.  
Später kann man das auch für Telemetrie, Logs oder Analyse nutzen (z. B. wann welche Medikamente eingenommen wurden, Compliance-Statistiken usw.).

**Beispielstruktur:**

Tabelle: patienten
- id (INTEGER, PRIMARY KEY)
- name
- geburtsdatum
- diagnose

Tabelle: medikamente
- id
- patient_id (Foreign Key)
- name
- zeit
- genommen (BOOLEAN)
Tabellen um Spalten wie „XP“, „Rad-Level“, „Status“ oder „letzte Änderung“ erweitern.  


## 🧩 2. Objektorientierte Struktur (OOP)

Das ist **der nächste logische Schritt**.  
Statt alles in einer Datei mit Funktionen zu halten, baut man in Klassen:

class Patient:
    def __init__(self, name, geburtsdatum, diagnose):
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.diagnose = diagnose
        self.medikamente = []
        self.rad_level = 0
        self.xp = 0
        self.rang = "Rookie"

class Medikament:
    def __init__(self, name, zeit, genommen=False):
        self.name = name
        self.zeit = zeit
        self.genommen = genommen

Das erlaubt später:

- **Methoden** wie `.nehme_medikament()`, `.erhöhe_rad_level()`
    
- **Automatische Datenbank-Synchronisation**
    
- **Verknüpfung mit GUI oder API**
    

Das System wird also skalierbar und wartbar.

## ☣️ 3. „Rad-Level“ (Stress-/Vergesslichkeitsindikator)


**Mechanik-Idee:**

- Ignorierst du 2 Erinnerungen → +1 Rad-Level
    
- Einnahme erfolgreich → -1 Rad-Level
    
- Bei Rad-Level ≥ 3 → Terminal gibt Warnung:  
    `"WARNUNG: Neuro-Strahlungswerte kritisch. Ruhe empfohlen."`
    
- Bei Rad-Level = 0 → `"Vault-Tec gratuliert! Mentale Reinheit erreicht."`
    

Später kann man das kombinieren mit **XP und Rängen**, z. B.:

| XP-Bereich | Rang             | Bonus                           |
| ---------- | ---------------- | ------------------------------- |
| 0–100      | Vault Rookie     | -                               |
| 101–250    | MedTech Initiate | kleiner Health-Bonus            |
| 251–500    | Security Officer | Zugriff auf „System Tools“      |
| 501+       | Vault Overseer   | Zugriff auf „Admin Terminal“ 🧠 |
Dadurch wird das Ganze zu einem **Mini-Rollenspielsystem** im medizinischen Kontext.  
Man kann XP direkt an Aktionen koppeln:

- Einnahme → +10 XP
    
- Ignorieren → -5 XP
    
- Neue Diagnose eintragen → +5 XP
    
- Tag ohne Fehler → +25 XP  
    → Progression + Selbstmotivation 💪
    

---

## 🔐 4. Eingabevalidierung & Security Layer##


- Regex-Prüfung (Datum, Uhrzeit, „ja/nein“)
    
- SQL-Escape vermeiden (mit `?`-Platzhaltern)
    
- Hash für sensible Daten (z. B. Medikamentenname)
    
- Optional AES-Verschlüsselung für SQLite-DB (später mit `sqlcipher` oder `cryptography`)
   

---

## 🐋 5. Containerisierung mit Docker


- Den ganzen Code isoliert ausführen
    
- Später sogar auf Raspberry Pi deployen
    
- Versionen kontrollieren
    
- Security-Scans (z. B. `trivy`) üben

Beispiel
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "vaultmed.py"]


## 🧩 **Stufe 1 – Fundament: Struktur & Datenbasis**

🎯 **Ziel:** Umstieg von Listen zu einer modularen, objektorientierten SQL-Lösung.  
 OOP-Grundprinzipien, SQLite-Einbindung, saubere Code-Struktur.

**Module:**

1. `patient.py` – Klasse `Patient` (Name, Geburtsdatum, Diagnose, XP, Rad-Level, Rang)
    
2. `medikament.py` – Klasse `Medikament` (Name, Zeit, Status)
    
3. `database.py` – SQLite-Connector mit CRUD-Funktionen
    
4. `main.py` – Zentrale Logik und Menüführung
    

**Zentrale Features:**

- Tabellen automatisch erstellen, falls nicht vorhanden
    
- Medikamente + Patienten speichern/laden
    
- Erste einfache CLI-Ausgabe im Fallout-Look
    

🧠 **Lernziel:** Verständnis von Klassen, Objekten, Beziehungen und Datenpersistenz.

---

## ☢️ **Stufe 2 – Gamification & Fallout-Charme**

🎯 **Ziel:** Motivationssysteme + Terminal-Ästhetik.

**Module:**

1. `xp_system.py` – XP-Berechnung & Ränge (Rookie → Overseer)
    
2. `rad_monitor.py` – Rad-Level mit Schwellenwerten & Warntexten
    
3. `ui_terminal.py` – ASCII-Interface, animierte Lade- und Statusanzeigen
    

**Zentrale Features:**

- XP-Belohnungen für Einnahme/Erfolg, Strafen für Vergessen
    
- Dynamische Rangbezeichnungen
    
- „Neuro-Strahlungs-Warnungen“ bei zu hohem Stresslevel
    
- Terminal-Intro im Vault-Tec-Stil (z. B. animiertes `[▓▓▓░░░░░] 47%`)
    

💡 **Option:** Sound- oder Text-Events bei Level-Ups (später über `pygame` oder Text-Delay simulieren).

---

## 🔐 **Stufe 3 – Security-Layer**

🎯 **Ziel:** Sicherheit, Integrität und Datenschutz.

**Module:**

1. `security.py` – Input-Validierung (Regex), Hashing (SHA256), Session-Prüfsumme
    
2. `sanitizer.py` – Eingabefilter, um Injection-Risiken zu vermeiden
    
3. `logger.py` – sicheres, rotierendes Logsystem mit optionaler Verschlüsselung
    

**Zentrale Features:**

- Datums-/Uhrzeit-Validierung
    
- Hashing sensibler Daten (z. B. Medikamentennamen)
    
- Session-Integrity-Hash
    
- Tamper-Detection für die DB (SHA-Prüfsumme beim Start)
    

💡 **Lernziel:** reale Security-Praktiken (Input-Härtung, Hashes, Checksums) 
---

## 🐋 **Stufe 4 – Containerisierung (Vault in a Box)**

🎯 **Ziel:** Lerne, das Programm sicher und reproduzierbar auszuführen.

**Module:**

1. `Dockerfile` – minimales Image mit Python-Setup
    
2. `requirements.txt` – Abhängigkeiten
    
3. `entrypoint.sh` – Startskript (führt VaultMed im Terminal aus)
    

**Zentrale Features:**

- Isolierte Laufumgebung
    
- Zugriff auf lokale Datenbank nur innerhalb des Containers
    
- Option: Health-Check-Script im Container („Vault-Status: Operational“)
    

💡 **Bonus:** Security-Scanner wie `trivy` oder `bandit` nutzen, um Schwachstellen zu analysieren.

---

## 💚 **Stufe 5 – Integration & Erweiterungen**

🎯 **Ziel:** VaultMed als Framework nutzen für anderen Projekte.

**Module / Optionen:**

1. `module_selfcare.py` – Anbindung an dein Self-Care-Terminal (Mood, Status, Energie)
    
2. `module_kaktoro.py` – Integration in den Neurodivers-Übersetzer (Feedback-Regelung)
    
3. `module_gummibaerenbande.py` – Erinnerungsmodul (GUI + XP-Sync)
    
4. `api_interface.py` – späterer REST- oder JSON-Export für GUI oder App
    

**Langfristige Vision:**

- Ein **universelles „VaultOS“-Framework**, das  Terminal-Systeme (Kevin, Self-Care, Kaktoro) miteinander verbindet.
    
- Jedes nutzt Module für Sicherheit, OOP, Datenbank und gamifizierte Selbstführung.
    

---




