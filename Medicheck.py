from datetime import datetime

# ANSI-Farbcodes für farbige Konsolenausgabe
FARBE_ROT = "\033[91m"
FARBE_GELB = "\033[93m"
FARBE_GRUEN = "\033[92m"
FARBE_ENDE = "\033[0m"


def ja_nein_frage(frage):
    """Stellt eine Ja/Nein-Frage und gibt True/False zurück."""
    antwort = input(frage + " (ja/nein): ").strip().lower()
    return antwort == "ja"


def eingabe_mit_label(label):
    """Fragt eine Eingabe mit Label ab."""
    return input(f"{label}: ")


# --- Patientendaten ---
NAME = eingabe_mit_label("PATIENTENNAME")
GEBURTSTAG = eingabe_mit_label("GEBURTSDATUM (TT.MM.JJJJ)")
DIAGNOSE = eingabe_mit_label("DIAGNOSEN")

print("\n--- Patientendaten ---")
print(f"Name: {NAME}")
print(f"Geburtsdatum: {GEBURTSTAG}")
print(f"Diagnose(n): {DIAGNOSE}")


# --- Medikamenten-Eingabe ---
anzahl = int(input("Wie viele Medikamente sollen überprüft werden? "))

medikamente = []

for i in range(anzahl):
    print(f"\nMedikament {i+1}:")
    name = eingabe_mit_label("Name des Medikaments")
    uhrzeit = eingabe_mit_label("Geplante Einnahmezeit (HH:MM)")
    genommen = ja_nein_frage("Wurde das Medikament heute bereits genommen?")
    
    medikamente.append({
        "name": name,
        "zeit": uhrzeit,
        "genommen": genommen
    })


# --- Aktuelle Uhrzeit ---
jetzt = datetime.now().strftime("%H:%M")


# --- Ausgabe & Erinnerung ---
print("\n--- Checkliste Medikamenteneinnahme ---")
noch_zu_nehmen = []

for medi in medikamente:
    name = medi["name"]
    zeit = medi["zeit"]
    genommen = medi["genommen"]

    if genommen:
        print(FARBE_GRUEN + f"{name} wurde bereits genommen." + FARBE_ENDE)
    else:
        if jetzt >= zeit:
            print(FARBE_GELB + f"Erinnerung: {name} sollte um {zeit} genommen werden!" + FARBE_ENDE)
            noch_zu_nehmen.append(f"{name} um {zeit}")
        else:
            print(f"{name} ist für später geplant ({zeit}).")


# --- Übersicht offener Einnahmen ---
if noch_zu_nehmen:
    print(FARBE_ROT + "\nNoch einzunehmende Medikamente heute:" + FARBE_ENDE)
    for eintrag in noch_zu_nehmen:
        print("- " + eintrag)
else:
    print(FARBE_GRUEN + "\nAlle Medikamente für jetzt wurden eingenommen!" + FARBE_ENDE)
