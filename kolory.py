import time, os
# Kody kolorów 
RESET = "\033[0m" #wraca do bialego, usuwa kolor
CZERWONY = "\033[91m"
ZIELONY = "\033[92m"
ZOLTY = "\033[93m"
NIEBIESKI = "\033[94m"
FIOLET = "\033[95m"
CYJAN = "\033[96m"

def czysc_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')#sprawdza system Windows (cls), Linux/Mac (clear)

def czekaj(sekundy):
    time.sleep(sekundy)

def drukuj_kolor(tekst, kolor):#teskt w kolorze i reset na end
    print(kolor + tekst + RESET)

def naglowek(tekst): 
    print(CYJAN + "=" * 60 + RESET)
    print(ZOLTY + f"{tekst.upper()}" + RESET)
    print(CYJAN + "=" * 60 + RESET)
