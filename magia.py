import random
from kolory import NIEBIESKI, CZERWONY, RESET, FIOLET, ZOLTY

def menu_zaklec(gracz):
    #4mana
    print(f"\n--- KSIEGA ZAKLEĆ (Twoja mana: {NIEBIESKI}{gracz[4]}{RESET}) ---")
    print("1. Kula Ognia (Koszt: 15 Mana, Obrazenia: 25-35)")
    print("2. Lodowy Pocisk (Koszt: 10 Mana, Obrazenia: 15-20)")
    print("3. Wyssanie Zycia (Koszt: 25 Mana, Atak: 15 + Leczenie)")
    print("0. Anuluj")
    
    wybor = input("\nWybierz zaklecie: ")
    
    if wybor == '1':
        return rzuc_ogien(gracz)
    elif wybor == '2':
        return rzuc_lod(gracz)
    elif wybor == '3':
        return rzuc_wyssanie_krwi(gracz)
    elif wybor == '0':
        return None
    else:
        print("Nie ma takiego zaklecia.")
        return None

def rzuc_ogien(gracz):
    koszt = 15
    if gracz[4] >= koszt:
        gracz[4] -= koszt
        dmg = random.randint(25, 35)
        print(f"\n{CZERWONY}>> OGROMNA KULA OGNIA uderza wroga! ({dmg} dmg){RESET}")
        return dmg
    else:
        print(f"\n{FIOLET}>> Masz za malo many!{RESET}")
        return 0

def rzuc_lod(gracz):
    koszt = 10
    if gracz[4] >= koszt:
        gracz[4] -= koszt
        dmg = random.randint(15, 20)
        print(f"\n{NIEBIESKI}>> LODOWY KOLEC przebija wroga! ({dmg} dmg){RESET}")
        return dmg
    else:
        print(f"\n{FIOLET}>> Masz za malo many!{RESET}")
        return 0

def rzuc_wyssanie_krwi(gracz):
    koszt = 25
    if gracz[4] >= koszt:
        gracz[4] -= koszt
        dmg = 15
        gracz[2] += dmg #+HP healing
        if gracz[2] > gracz[3]: #check max HP
            gracz[2] = gracz[3]
        print(f"\n{ZOLTY}>> MROCZNA MAGIA kradnie zycie wroga! (+{dmg} HP dla Cb){RESET}")
        return dmg
    else:
        print(f"\n{FIOLET}>> Masz za malo many!{RESET}")
        return 0
