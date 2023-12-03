zlecenia = []

def dodaj_zlecenie(nazwa, lokalizacja, cena):
    zlecenie = {
        'nazwa': nazwa,
        'lokalizacja': lokalizacja,
        'cena': cena
    }
    zlecenia.append(zlecenie)

def wyswietl_nowe_zlecenia():
    if len(zlecenia) > 0:
        print("Nowe zlecenia:")
        for idx, zlecenie in enumerate(zlecenia[-1:], start=len(zlecenia)):
            print(f"{idx}. {zlecenie['nazwa']} - {zlecenie['lokalizacja']} - {zlecenie['cena']}")
    else:
        print("Brak nowych zleceń.")

def wyswietl_wszystkie_zlecenia():
    if len(zlecenia) > 0:
        print("Wszystkie zlecenia:")
        for idx, zlecenie in enumerate(zlecenia, start=1):
            print(f"{idx}. {zlecenie['nazwa']} - {zlecenie['lokalizacja']} - {zlecenie['cena']}")
    else:
        print("Brak dostępnych zleceń.")

while True:
    print("\n1. Dodaj zlecenie")
    print("2. Wyświetl nowe zlecenia")
    print("3. Wyświetl wszystkie zlecenia")
    print("4. Wyjdź")

    wybor = input("Wybierz opcję (1/2/3/4): ")

    if wybor == '1':
        nazwa = input("Podaj nazwę zlecenia: ")
        lokalizacja = input("Podaj lokalizację: ")
        cena = input("Podaj cenę: ")

        dodaj_zlecenie(nazwa, lokalizacja, cena)
        print("Zlecenie dodane pomyślnie.")

    elif wybor == '2':
        wyswietl_nowe_zlecenia()

    elif wybor == '3':
        wyswietl_wszystkie_zlecenia()

    elif wybor == '4':
        break

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
