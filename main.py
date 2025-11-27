
from database import init_db
from patient import Patient
from medikament import Medikament
from vault_utils import vault_intro, FARBE_GRUEN, FARBE_GELB, FARBE_ENDE, slow_print
import random
from datetime import datetime
from input_utils import eingabe_int, eingabe_zeit, eingabe_text, ja_nein
from security import pruefe_integritaet, get_in tegritaets_fehler_meldung, aktualisiere_integritaet

anzahl = eingabe_int("Wie viele Medikamente sollen heute überprüft werden?")
m_name = eingabe_text("Name")
m_zeit = eingabe_zeit("Uhrzeit")
m_genommen = ja_nein("Schon genommen?")

sprüche_motivierend = [
    "Jede Dosis bringt dich näher zur Genesung, Paladin.",
    "Deine Gesundheit ist deine größte Waffe gegen die Ödnis.",
    "Bleib stark, Bruder! Jeder eingenommene Stimpack zählt.",
    "Die Ödnis mag hart sein, aber du bist härter!",
    "Deine Entschlossenheit ist der Schlüssel zur Heilung.",
]

sprüche_mahnend = [
    "Vergiss nicht deine Stimpacks – die Ödnis wartet nicht.",
    "Jeder verpasste Stimpack bringt dich näher an den Abgrund.",
    "Deine Gesundheit ist kein Spiel – handle rechtzeitig!",
    "Willst du zu einem Ghoul werden? Dann vergiss deine Stimpacks!",
]


def main():
    vault_intro()
    init_db()
#---Hier die Sicherheitsprüfung---
    if not pruefe_integritaet():
        slow_print(FARBE_ROT + get_integritaets_fehler_meldung() + FARBE_ENDE , delay=0.05)
        
    print("Willkommen im Vault-Tec Terminal.")
    name = input("Name des Vault-Bewohners: ").strip()
    patient = Patient.laden(name)

    if not patient:
        print(FARBE_GELB + "Neues Profil wird angelegt..." + FARBE_ENDE)
        geb = input("Geburtsdatum (TT.MM.JJJJ): ").strip()
        diag = input("Diagnose(n): ").strip()
        patient = Patient(name, geb, diag)
        patient.speichern()

    patient.anzeigen()

    # Medikamente des Tages
    anzahl = int(input("\nWie viele Medikamente sollen heute überprüft werden? "))
    for i in range(anzahl):
        print(f"\nMEDIKAMENT {i+1}:")
        m_name = input("Name: ").strip()
        m_zeit = input("Uhrzeit (HH:MM): ").strip()
        m_genommen = input("Schon genommen? (ja/nein): ").lower() == "ja"

        medi = Medikament(m_name, m_zeit, m_genommen)
        patient.add_medikament(medi)

        # Motivation / Mahnung
        if m_genommen:
            print(FARBE_GRUEN + random.choice(sprüche_motivierend) + FARBE_ENDE)
        else:
            jetzt = datetime.now().strftime("%H:%M")
            if jetzt >= m_zeit:
                print(FARBE_GELB + f"Erinnerung: {m_name} sollte um {m_zeit} genommen werden!" + FARBE_ENDE)
                print(FARBE_ROT + random.choice(sprüche_mahnend) + FARBE_ENDE)

    print(FARBE_GRUEN + "\nVault-Synchronisierung abgeschlossen. Daten sicher gespeichert." + FARBE_ENDE)


if __name__ == "__main__":
    main()
    aktualisiere_integritaet()

    print(FARBE_GRUEN + "\nVault-Syncronisierung agbeschlossen. Daten sicher gespeichert." + FARBE_ENDE)
    




