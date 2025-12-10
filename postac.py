from kolory import ZIELONY, NIEBIESKI, RESET, naglowek, czysc_ekran, czekaj, ZOLTY, CZERWONY, FIOLET, CYJAN
def stworz_gracza():
    czysc_ekran()
    naglowek("Kreator Postaci")
    print("Witaj w świecie uzytkowniku.")
    imie = input("Podaj imię swojego bohatera: ")
    
    if len(imie) == 0:
        imie = "Bezimienny"
    gracz =[
        imie,
        1,#1.lvl
        100,#2.HP
        100,#3.maxHP
        40,#4.mana
        40,#5.maxmana
        10,#6.dmg
        20,#7.zloto
        0,#8.exp
        100,#9.expdonext
        3#10.potki
]
    
    print(f"\nWitaj, {ZIELONY}{gracz[0]}{RESET}! Twoja przygoda się zaczyna...")
    czekaj(1)
    return gracz

def pokaz_statystyki(gracz):
    print(CYJAN + "-" * 60 + RESET)
    print(f" BOHATER: {ZOLTY}{gracz[0]}{RESET} | ZŁOTO: {ZOLTY}{gracz[7]}{RESET} ")
    
    kolor_hp = ZIELONY#HP2
    if gracz[2] < 30:
        kolor_hp = CZERWONY    
    print(f" ZDROWIE: {kolor_hp}{gracz[2]}/{gracz[3]}{RESET} | MANA: {NIEBIESKI}{gracz[4]}/{gracz[5]}{RESET}")
    print(f" POZIOM: {gracz[1]} | EXP: {gracz[8]}/{gracz[9]}")
    print(f" SIŁA: {gracz[6]} | MIKSTURY: {FIOLET}{gracz[10]}{RESET}")
    print(CYJAN + "-" * 60 + RESET)

def sprawdz_awans(gracz):
    # 8EXP,9EXPdonext
    if gracz[8] >= gracz[9]:
        gracz[1] += 1#nextlvl,1lvl
        gracz[8] -= gracz[9]
        gracz[9] = int(gracz[9] * 1.5)
        
        # +staty
        gracz[3] += 20  #max HP
        gracz[5] += 10  #max mana
        gracz[6] += 3   #atak
        
        # leczenie
        gracz[2] = gracz[3] # HP = max HP
        gracz[4] = gracz[5] # Mana = Max Mana
        
        print("\n" + ZOLTY + "*" * 40)
        print(f" GRATULACJE! OSIAGNALES POZIOM {gracz[1]}!")
        print("*" * 40 + RESET)
        input("\nNacisnij ENTER...")

def uzyj_mikstury(gracz):
    # gracz10 mikstury
    if gracz[10] > 0:
        leczenie = 50
        gracz[10] -= 1
        gracz[2] += leczenie # +HP
        
        if gracz[2] > gracz[3]:
            gracz[2] = gracz[3]
            
        print(f"\n{ZIELONY}>> Wypiłes miksture. Odzyskujesz {leczenie} HP.{RESET}")
        return True
    else:
        print(f"\n{CZERWONY}>> Nie masz mikstur!{RESET}")
        return False
