import random
from kolory import czysc_ekran, naglowek, czekaj, ZIELONY, RESET, CZERWONY, drukuj_kolor
from postac import stworz_gracza, pokaz_statystyki, uzyj_mikstury
from walka import bitwa
from kolory import ZOLTY, FIOLET, CYJAN
def sklep(gracz):
    # gracz[7] = zloto, gracz[10] = mikstury, gracz[4/5] = mana, gracz[6] = atak
    while True:
        czysc_ekran()
        naglowek(f"sklep wedrowca (Zloto: {gracz[7]})")
        print("1. Mikstura Leczenia (+50 HP)  - 20 zlota")
        print("2. Mikstura Many (+40 Mana)    - 15 zlota")
        print("3. Ostrzenie miecza (+2 Atak)  - 50 zlota")
        print("4. Wyjdź")
        
        wybor = input("\nCo chcesz kupic? ")
         
        if wybor == '1':
            if gracz[7] >= 20:
                gracz[7] -= 20
                gracz[10] += 1
                drukuj_kolor("Kupiono miksture!", ZIELONY)
            else:
                print("Brak zlota!")
            czekaj(1)
            
        elif wybor == '2':
            if gracz[7] >= 15:
                gracz[7] -= 15
                gracz[4] += 40
                if gracz[4] > gracz[5]: gracz[4] = gracz[5]
                drukuj_kolor("Wypito eliksir many!", ZIELONY)
            else:
                print("Brak zlota!")
            czekaj(1)
            
        elif wybor == '3':
            if gracz[7] >= 50:
                gracz[7] -= 50
                gracz[6] += 2
                drukuj_kolor("Naostrzono Twoj miecz!", ZIELONY)
            else:
                print("Brak zlota!")
            czekaj(1)
            
        elif wybor == '4':
            break

def eksploracja(gracz):
    czysc_ekran()
    print("Wyruszasz w daleka podroz...")
    czekaj(1)
    
    los = random.randint(1, 100)
    
    if los <= 50:
        wynik = bitwa(gracz)
        if wynik == "smierc":
            return "koniec"
            
    elif los <= 75:
        znalezione = random.randint(10, 30)
        gracz[7] += znalezione # zloto
        print(f"\n{ZIELONY}Znajdujesz zgubiona sakiewke! +{znalezione} zlota.{RESET}")
        input("\nNacisnij ENTER...")
        
    elif los <= 85:
        print("\nZnajdujesz bezpieczny kat.")
        print("Odpoczywasz chwile, Twoje HP i mana rosna.")
        gracz[2] += 20 # hp
        gracz[4] += 10 # mana
        if gracz[2] > gracz[3]: 
            gracz[2] = gracz[3] # max hp spr
        if gracz[4] > gracz[5]: 
            gracz[4] = gracz[5] # max mana spr
        input("\nNacisnij ENTER...")
        
    else:
        print("\nNic sie nie dzieje. Cisza i spokoj.")
        input("\nNaciśnij ENTER...")
    
    return "dalej"

def main():
    try:
        gracz = stworz_gracza()
        
        gra_trwa = True
        while gra_trwa:
            czysc_ekran()
            naglowek("menu glowne")
            pokaz_statystyki(gracz)
            
            print("\nCo chcesz zrobic?")
            print("1. Wyrusz na wyprawe (Eksploracja)")
            print("2. Odwiedź Miasto (Sklep)")
            print("3. Wypij miksture")
            print("4. Zakoncz gre")
            
            wybor = input("\nTwoj wybor: ")
            
            if wybor == '1':
                wynik = eksploracja(gracz)
                if wynik == "koniec":
                    gra_trwa = False
            elif wybor == '2':
                sklep(gracz)
            elif wybor == '3':
                uzyj_mikstury(gracz)
                czekaj(1)
            elif wybor == '4':
                czekaj(0.8)
                print("\nDo zobaczenia...")
                czekaj(1)
                gra_trwa = False
            else:
                continue
        
        czysc_ekran()
        print(CZERWONY + "X" * 50)
        print(" "*18 + "GAME OVER")
        print("X"*50 + RESET)
        
        print(CYJAN + "-=-" *16+ "=-")
        print(" "*10 + "TWOJE KONCOWE STATYTSTYKI "+RESET)#1lvl,7zloto,8exp,9expdonext,10mikstury
        print(f"POZIOM: {gracz[1]}{RESET} | EXP: {gracz[8]}/{gracz[9]} \nZLOTO: {ZOLTY}{gracz[7]}{RESET} | MIKSTURY: {FIOLET}{gracz[10]}{RESET}")
        print(CYJAN+"-=-"*16 +"=-"+ RESET)

        inp = input("\nCzy chcesz zagrac ponownie?(t/n) ")
        if inp.lower().strip() == "t":
            main()
        else:
            pass
    except KeyboardInterrupt:#jak sie przerwie to nie wywala erroru
        print("\nPrzerwano grę.")

main()
