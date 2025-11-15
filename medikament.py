from database import get_connection

class Medikament:
    def __init__(self, name, zeit, genommen=False, id=None):
        self.id = id
        self.name = name
        self.zeit = zeit
        self.genommen = genommen

    def speichern(self, patient_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO medikamente (patient_id, name, zeit, genommen)
            VALUES (?, ?, ?, ?)
        """, (patient_id, self.name, self.zeit, int(self.genommen)))
        conn.commit()
        conn.close()

    @staticmethod
    def lade_alle(patient_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medikamente WHERE patient_id=?", (patient_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Medikament(row[2], row[3], bool(row[4]), id=row[0]) for row in rows]

    def __repr__(self):
        status = "✅" if self.genommen else "⚠️"
        return f"{self.name} um {self.zeit} {status}"
