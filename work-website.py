zlecenia = []

def dodaj_zlecenie(nazwa, lokalizacja, cena):
    zlecenie = {
        'nazwa': nazwa,
        'lokalizacja': lokalizacja,
        'cena': cena
    }
    zlecenia.append(zlecenie)

def wyswietl_zlecenia():
    print("Dostępne zlecenia:")
    for idx, zlecenie in enumerate(zlecenia, start=1):
        print(f"{idx}. {zlecenie['nazwa']} - {zlecenie['lokalizacja']} - {zlecenie['cena']}")

while True:
    print("\n1. Dodaj zlecenie")
    print("2. Wyświetl zlecenia")
    print("3. Wyjdź")

    wybor = input("Wybierz opcję (1/2/3): ")

    if wybor == '1':
        nazwa = input("Podaj nazwę zlecenia: ")
        lokalizacja = input("Podaj lokalizację: ")
        cena = input("Podaj cenę: ")

        dodaj_zlecenie(nazwa, lokalizacja, cena)
        print("Zlecenie dodane pomyślnie.")

    elif wybor == '2':
        wyswietl_zlecenia()

    elif wybor == '3':
        break

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")