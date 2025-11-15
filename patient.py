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
                UPDATE patienten 
                SET name=?, geburtsdatum=?, diagnose=?, xp=?, rad_level=?, rang=?
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

        if not row:
            conn.close()
            return None

        patient = Patient(*row[1:], id=row[0])

        # Medikamente laden
        cursor.execute("SELECT name, zeit, genommen FROM medikamente WHERE patient_id=?", (patient.id,))
        meds = cursor.fetchall()
        conn.close()

        for m in meds:
            name, zeit, genommen = m
            patient.medikamente.append(Medikament(name, zeit, bool(genommen)))

        return patient

    def add_medikament(self, medikament):
        self.medikamente.append(medikament)
        medikament.speichern(self.id)

     def anzeigen(self):
        print("\n=== 🛡️  VAULT-TEC PATIENTENPROFIL  🛡️ ===")
        print(f"Name: {self.name}")
        print(f"Geburtsdatum: {self.geburtsdatum}")
        print(f"Diagnose: {self.diagnose}")
        print(f"XP: {self.xp}   |   Rang: {self.rang}   |   RAD-Level: {self.rad_level}")
        print("\nAktuelle Medikamente:")
        if not self.medikamente:
            print("  - Keine eingetragen.")
        else:
            for m in self.medikamente:
                print("  -", m)

    def add_xp(self, amount: int):
        self.xp += amount
        self.update_rang()
        self.speichern()

    def update_rang(self):
        if self.xp >= 1000:
            self.rang = "Elder"
        elif self.xp >= 500:
            self.rang = "Paladin"
        elif self.xp >= 300:
            self.rang = "Ranger"
        elif self.xp >= 150:
            self.rang = "Wanderer"
        elif self.xp >= 50:
            self.rang = "Scout"
        else:
            self.rang = "Rookie"

    def add_rad(self, amount: int):
        self.rad_level += amount
        if self.rad_level < 0:
            self.rad_level = 0
        self.speichern()

    def einnahme_erfolgreich(self, rechtzeitig=True):
        if rechtzeitig:
            self.add_xp(10)
            self.add_rad(-1)
        else:
            self.add_xp(2)
            self.add_rad(-1)

    def einnahme_verpasst(self):
        self.add_xp(-5)
        self.add_rad(+1)


