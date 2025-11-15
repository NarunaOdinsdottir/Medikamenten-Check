import time
import sys

FARBE_GRUEN = "\033[92m"
FARBE_GELB = "\033[93m"
FARBE_CYAN = "\033[96m"
FARBE_ENDE = "\033[0m"

def vault_intro():
    print(FARBE_CYAN + "\nVault-Tec Secure Health Terminal v0.1".center(60, "-") + FARBE_ENDE)
    for i in range(0, 101, 10):
        time.sleep(0.05)
        sys.stdout.write(f"\rInitialisierung: {i}%")
        sys.stdout.flush()
    print("\nSystemstatus: STABIL ✅\n")

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
