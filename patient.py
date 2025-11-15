from medikament import Medikament
from database import get_connection

class Patient:
    def __init__(self, name, geburtsdatum, diagnose, xp=0, rad_level=0, rang="Rookie", id=None):
        self.id = id
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.diagnose = diagnose
        self.xp = xp
        self.rad_level = rad_level
        self.rang = rang
        self.medikamente = []

    def speichern(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO patienten (name, geburtsdatum, diagnose, xp, rad_level, rang)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.name, self.geburtsdatum, self.diagnose, self.xp, self.rad_level, self.rang))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE patienten SET name=?, geburtsdatum=?, diagnose=?, xp=?, rad_level=?, rang=?
                WHERE id=?
            """, (self.name, self.geburtsdatum, self.diagnose, self.xp, self.rad_level, self.rang, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def laden(name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patienten WHERE name=?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Patient(*row[1:], id=row[0])
        return None

    def add_medikament(self, medikament):
        self.medikamente.append(medikament)
        medikament.speichern(self.id)

    def anzeigen(self):
        print(f"\n=== VAULT-TEC PATIENTENPROFIL ===")
        print(f"Name: {self.name}")
        print(f"Geburtsdatum: {self.geburtsdatum}")
        print(f"Diagnose: {self.diagnose}")
        print(f"XP: {self.xp} | Rang: {self.rang} | Rad-Level: {self.rad_level}")
