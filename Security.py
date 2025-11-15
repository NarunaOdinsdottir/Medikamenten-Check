# security.py
import hashlib
import os

DB_NAME = "vaultmed.db"
HASH_FILE = "vaultmed.hash"

def berechne_sha256(dateiname):
    """Berechnet den SHA256-Hash einer Datei."""
    hasher = hashlib.sha256()
    # Chunk-weise lesen, um auch große Dateien zu unterstützen
    try:
        with open(dateiname, 'rb') as datei:
            while True:
                chunk = datei.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        # DB existiert noch nicht (erster Start)
        return None

def pruefe_integritaet():
    """
    Prüft, ob der aktuelle Hash der Datenbank mit dem gespeicherten Hash übereinstimmt.
    """
    # 1. Aktuellen Hash der Datenbank berechnen
    aktueller_hash = berechne_sha256(DB_NAME)

    # 2. Gespeicherten Hash laden
    gespeicherter_hash = None
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            gespeicherter_hash = f.read().strip()

    # 3. Ergebnis auswerten

    # Fall 1: Erster Start oder Hash-Datei gelöscht
    if aktueller_hash and gespeicherter_hash is None:
        print("\n[SECURITY] Initialer Datenbank-Hash erstellt.")
        speichere_hash(aktueller_hash)
        return True

    # Fall 2: Datenbank existiert nicht (auch OK, wird neu erstellt)
    if aktueller_hash is None:
        return True

    # Fall 3: Integritätsprüfung
    if aktueller_hash == gespeicherter_hash:
        return True
    else:
        # Manipulations-Alarm!
        return False

def speichere_hash(aktueller_hash):
    """Speichert den aktuellen Hash in einer separaten Datei."""
    with open(HASH_FILE, 'w') as f:
        f.write(aktueller_hash)

def aktualisiere_integritaet(db_verbindung=None):
    """
    Wird nach dem Speichern kritischer Daten aufgerufen,
    um den Hash-Wert neu zu berechnen und zu speichern.
    """
    # SQLite-Verbindung schließen, um sicherzustellen, dass alle Daten auf der Platte sind
    if db_verbindung:
        db_verbindung.close()

    neuer_hash = berechne_sha256(DB_NAME)
    if neuer_hash:
        speichere_hash(neuer_hash)

# Prüfungslogik, falls die DB manipuliert wurde
def get_integritaets_fehler_meldung():
    return "\n❌ INKONSISTENZ ALARM ❌\nDie Datenbank wurde seit dem letzten Start manipuliert. Systemintegrität gefährdet!"
