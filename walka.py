import random
from kolory import czysc_ekran, czekaj, CZERWONY, ZIELONY, ZOLTY, RESET
from postac import pokaz_statystyki, uzyj_mikstury, sprawdz_awans
from magia import menu_zaklec

def generuj_wroga(poziom_gracza):
    imiona = ["Wsciekly Szczur", "Goblin Zlodziej", "Wilk", "Szkielet", "Ork", "Mroczny Rycerz"]
    
    if poziom_gracza < 3:
        nazwa = random.choice(imiona[0:3])
        hp = random.randint(20, 40)
        atak = random.randint(3, 8)
        exp = 30
        zloto = 10
    elif poziom_gracza < 6:
        nazwa = random.choice(imiona[2:5])
        hp = random.randint(50, 90)
        atak = random.randint(8, 15)
        exp = 70
        zloto = 30
    else:
        nazwa = random.choice(imiona[4:])
        hp = random.randint(100, 200)
        atak = random.randint(15, 25)
        exp = 150
        zloto = 60

    # lista wroga:
    return [nazwa, hp, hp, atak, exp, zloto]

def bitwa(gracz):
    # 1lvl
    wrog = generuj_wroga(gracz[1])
    
    czysc_ekran()
    print(CZERWONY + "!!!" + " " * 50 + "!!!")
    print(" "*10 + f"ZAATAKOWAŁ CIE: {wrog[0]}")
    print("!!!" + " " * 50 + "!!!" + RESET)
    czekaj(1.5)

    walka_trwa = True
    
    while walka_trwa:
        czysc_ekran()
        pokaz_statystyki(gracz)
        
        # wrog.nazwa0, wrog.HP1, wrog.max.HP2
        print(f"\n PRZECIWNIK: {CZERWONY}{wrog[0]}{RESET}")
        print(f" HP WROGA: {wrog[1]} / {wrog[2]}")
        print("-" * 30)
        
        print("1. Atak mieczem")
        print("2. Magia")
        print("3. Mikstura")
        print("4. Ucieczka")
        
        wybor = input("\nCo robisz? ")
        tura_wykonana = False
        
        if wybor == '1':
            # 6atak
            dmg = gracz[6] + random.randint(-2, 3)
            wrog[1] -= dmg
            print(f"\n>> Atakujesz mieczem i zadajesz {dmg} obrazen!")
            tura_wykonana = True
            
        elif wybor == '2':
            obrazenia = menu_zaklec(gracz)
            if obrazenia is not None:
                if obrazenia > 0:
                    wrog[1] -= obrazenia
                tura_wykonana = True
            else:
                tura_wykonana = False
                
        elif wybor == '3':
            if uzyj_mikstury(gracz):
                tura_wykonana = True
            else:
                czekaj(1)
                
        elif wybor == '4':
            szansa = random.randint(1, 10)
            if szansa > 4:
                print(f"\n{ZIELONY}>> Udalo Ci sie uciec!{RESET}")
                czekaj(1)
                return "ucieczka"
            else:
                print(f"\n{CZERWONY}>> Potknales sie! Ucieczka nieudana.{RESET}")
                czekaj(1)
                tura_wykonana = True
        else:
            print("Nieprawidlowy wybor.")

        # wrog zyje? 
        if wrog[1] <= 0:
            print(f"\n{ZOLTY}ZWYCIESTWO! {wrog[0]} zostal pokonany!{RESET}")
            # gracz[7] to złoto, gracz[8] to exp
            gracz[7] += wrog[5]
            gracz[8] += wrog[4]
            print(f"Zdobywasz {wrog[5]} zlota i {wrog[4]} doswiadczenia.")
            czekaj(2)
            sprawdz_awans(gracz)
            return "wygrana"

        if tura_wykonana:
            print("\n... Tura przeciwnika ...")
            czekaj(0.8)
            # wrog3atak
            dmg_wroga = wrog[3] + random.randint(-1, 2)
            if dmg_wroga < 0: 
                dmg_wroga = 0
            
            # g2HP
            gracz[2] -= dmg_wroga
            print(f"{CZERWONY}>> {wrog[0]} atakuje Cie za {dmg_wroga} obrazen!{RESET}")
            czekaj(1.5)
            
            if gracz[4] < gracz[5]:#mana
                gracz[4] += 2

            if gracz[2] <= 0:
                return "smierc"
