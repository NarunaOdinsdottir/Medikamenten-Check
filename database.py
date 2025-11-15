import sqlite3

DB_NAME = "vaultmed.db"

def init_db():
    """Erstellt Datenbanktabellen, falls sie noch nicht existieren."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patienten (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        geburtsdatum TEXT NOT NULL,
        diagnose TEXT,
        xp INTEGER DEFAULT 0,
        rad_level INTEGER DEFAULT 0,
        rang TEXT DEFAULT 'Rookie'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medikamente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        name TEXT NOT NULL,
        zeit TEXT NOT NULL,
        genommen INTEGER DEFAULT 0,
        FOREIGN KEY(patient_id) REFERENCES patienten(id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aktion TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        details TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ranks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        min_xp INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def get_connection():
    """Erstellt eine neue DB-Verbindung."""
    return sqlite3.connect(DB_NAME)
