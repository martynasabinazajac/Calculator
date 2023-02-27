
import logging
logging.basicConfig(level=logging.INFO)


def calculator(option, x, y):
    if option == 1:
        logging.info(f'Dodaję: {x} i {y}')
        return x + y
    elif option == 2:
        logging.info(f'Odejmuję: od {x} liczbę {y}')
        return x - y
    elif option == 3:
        logging.info(f'Mnożę: {x} i {y}')
        return x * y
    elif option == 4:
        logging.info(f'Dzielę: {x} przez {y}')
        return x / y
    else:
        print('Operacja nie możliwa. Brak wybranego działania z dostepnych opcji.')
        exit(1)

if __name__=="__main__":
    option = int(input(
    'Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
    x = float(input("podaj pierwsza liczbę:"))
    y = float(input("podaj druga liczbę:"))
    result = calculator(option, x, y)
    print(f'Wynik to: {result}')
