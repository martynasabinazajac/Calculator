import logging
logging.basicConfig(level=logging.INFO)


def calculator(x, y):
    if option == 1:
        logging.info('Dodaję: %0.2f i %0.2f' % (x, y))
        return x + y
    elif option == 2:
        logging.info('Odejmuję: %0.2f od %0.2f' % (x, y))
        return x - y
    elif option == 3:
        logging.info('Mnożę: %0.2f i %0.2f' % (x, y))
        return x * y
    elif option == 4:
        logging.info('Dzielę: %0.2f przez %0.2f' % (x, y))
        return x / y
    else:
        print('Operacja nie możliwa. Brak wybranego działania z dostepnych opcji.')
        exit(1)


option = int(input(
    'Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
x = float(input("podaj pierwsza liczbę:"))
y = float(input("podaj druga liczbę:"))
result = calculator(x, y)
print('Wynik to: %0.2f' %result)
