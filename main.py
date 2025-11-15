from database import init_db
from patient import Patient
from medikament import Medikament
from vault_utils import vault_intro, FARBE_GRUEN, FARBE_GELB, FARBE_ENDE

def main():
    vault_intro()
    init_db()

    print("Willkommen im Vault-Tec Terminal.")
    name = input("Name des Vault-Bewohners: ").strip()
    patient = Patient.laden(name)

    if not patient:
        print(FARBE_GELB + "Neues Profil wird angelegt..." + FARBE_ENDE)
        geb = input("Geburtsdatum (TT.MM.JJJJ): ")
        diag = input("Diagnose(n): ")
        patient = Patient(name, geb, diag)
        patient.speichern()

    patient.anzeigen()

    anzahl = int(input("\nWie viele Medikamente sollen heute überprüft werden? "))
    for i in range(anzahl):
        print(f"\nMEDIKAMENT {i+1}:")
        m_name = input("Name: ")
        m_zeit = input("Uhrzeit (HH:MM): ")
        m_genommen = input("Schon genommen? (ja/nein): ").lower() == "ja"
        medi = Medikament(m_name, m_zeit, m_genommen)
        patient.add_medikament(medi)

    print("\n--- AKTUELLER STATUS ---")
    for m in patient.medikamente:
        print("-", m)

    print(FARBE_GRUEN + "\nVault-Synchronisierung abgeschlossen. Daten sicher gespeichert." + FARBE_ENDE)

if __name__ == "__main__":
    main()
