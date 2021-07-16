X = "X"
O = "O"
pusty = " "
remis = "Remis"
liczba_pol = 9

# tworzenie tablicy gry
def tablica_gry (tablica):
    print(tablica[0], "|", tablica[1], "|", tablica[2])
    print("---------")
    print(tablica[3], "|", tablica[4], "|", tablica[5])
    print("---------")
    print(tablica[6], "|", tablica[7], "|", tablica[8], "\n")
    
# nowa tablica gry
def nowa_tablica():
    tablica = []
    for pole in range(liczba_pol):
        tablica.append(pusty)
    return tablica

# wybieranie kto pierwszy zaczyna
def kto_pierwszy():
    computer = X
    czlowiek = O
    return computer, czlowiek

# dozwolone ruchy w grze
def dozwolone_ruchy (tablica):
    ruch = []
    for pole in range(liczba_pol):
        if tablica[pole] == pusty:
            ruch.append(pole)
    return ruch

# układ wygrywających lini
def wygrywajacy_uklad(tablica):
    wygrywajace_linie = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
                        )
    
    for rzad in wygrywajace_linie:
        if tablica[rzad[0]] == tablica[rzad[1]] == tablica[rzad[2]] != pusty:
            wygrany = tablica[rzad[0]]
            return wygrany

    if pusty not in tablica:
        return remis

    return None

# wybieranie pola do postawienia swojego znaku
def zapytaj_o_liczbe(pytanie, niska, wysoka):
    odpowiedz = None
    while odpowiedz not in range(niska, wysoka):
        odpowiedz = int(input(pytanie))
    return odpowiedz

# ruch człowieka przy wybieraniu pola
def ruch_czlowieka(tablica, czlowiek):
    prawidlowy = dozwolone_ruchy(tablica)
    ruch = None
    while ruch not in prawidlowy:
        ruch = zapytaj_o_liczbe("Twój ruch? (0 - 8):", 0, liczba_pol)
        if ruch not in prawidlowy:
            print("\nTo pole jest zajęte. Wybierz inne.\n")
    print("Lepiej...")
    return ruch

# zmiana kolejki
def zmiana_gracz(zmiana):
    if zmiana == X:
        return O
    else:
        return X

# ruchy komputera
def ruch_computera(tablica, computer, czlowiek):
    # kopię roboczą, ponieważ funkcja będzie zmieniać listę
    tablica = tablica[:]
    najlepsze_ruchy = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Wybieram pole numer", end=" ")
    
    # jeśli komputer może wygrać, wykonaj ten ruch
    for ruch in dozwolone_ruchy(tablica):
        tablica[ruch] = computer
        if wygrywajacy_uklad(tablica) == computer:
            print(ruch)
            return ruch
        # ten ruch został sprawdzony, wycofaj go
        tablica[ruch] = pusty
    
    # jeśli człowiek może wygrać, zablokuj ten ruch
    for ruch in dozwolone_ruchy(tablica):
        tablica[ruch] = czlowiek
        if wygrywajacy_uklad(tablica) == czlowiek:
            print(ruch)
            return ruch
        # ten ruch został sprawdzony, wycofaj go
        tablica[ruch] = pusty

    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for ruch in najlepsze_ruchy:
        if ruch in dozwolone_ruchy(tablica):
            print(ruch)
            return ruch

# podziekowania dla zwycięzcy
def zwyciezca(wygrany, computer, czlowiek):
    if wygrany != remis:
        print(wygrany, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")

    if wygrany == computer:
        print("Computer okazał się lepszy.")

    elif wygrany == czlowiek:
        print("Czlowiek okazał się lepszy.")

    elif wygrany == remis:
        print("Mamy remis")

# gra właściwa
def gra():
    computer, czlowiek = kto_pierwszy()
    zmiana = X
    tablica = nowa_tablica()
    tablica_gry(tablica)

    while not wygrywajacy_uklad(tablica):
        if zmiana == czlowiek:
            ruch = ruch_czlowieka(tablica, czlowiek)
            tablica[ruch] = czlowiek
        else:
            ruch = ruch_computera(tablica, computer, czlowiek)
            tablica[ruch] = computer
        tablica_gry(tablica)
        zmiana = zmiana_gracz(zmiana)

    wygrany = wygrywajacy_uklad(tablica)
    zwyciezca(wygrany, computer, czlowiek)

print (gra())
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")
