def eingabe_int(label: str):
    """Sichert ab, dass der Nutzer eine Zahl eingibt."""
    while True:
        wert = input(f"{label}: ").strip()
        if wert.isdigit():
            return int(wert)
        print("❌ Bitte gib eine gültige Zahl ein.")


def eingabe_zeit(label: str):
    """Validiert HH:MM Eingaben."""
    while True:
        zeit = input(f"{label} (HH:MM): ").strip()
        if len(zeit) == 5 and zeit[2] == ":":
            hh, mm = zeit.split(":")
            if hh.isdigit() and mm.isdigit():
                h = int(hh)
                m = int(mm)
                if 0 <= h < 24 and 0 <= m < 60:
                    return zeit
        print("❌ Ungültige Zeit. Beispiel: 08:30")


def eingabe_text(label: str):
    """Ein normaler Text (nicht leer)."""
    while True:
        txt = input(f"{label}: ").strip()
        if txt:
            return txt
        print("❌ Dieses Feld darf nicht leer sein.")


def ja_nein(label: str):
    """Fragt eine Ja/Nein-Eingabe ab."""
    while True:
        antw = input(f"{label} (ja/nein): ").strip().lower()
        if antw in ("ja", "j"):
            return True
        if antw in ("nein", "n"):
            return False
        print("❌ Bitte mit JA oder NEIN antworten.")
