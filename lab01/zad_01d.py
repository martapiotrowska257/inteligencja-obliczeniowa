import datetime
import math

name = input('Jak się nazywasz? ')
year = int(input('Podaj rok urodzenia: '))
month = int(input('Podaj miesiąc urodzenia: '))
day = int(input('Podaj dzień urodzenia: '))

birthday = datetime.datetime(year, month, day)
todays_date = datetime.datetime.now()

t = (todays_date - birthday).days  # ilość dni życia od narodzin

# obliczanie biorytmów
def calculate_biorhythm(days_lived, cycle_length):
    return math.sin(((2 * math.pi) / cycle_length) * days_lived)

physical = calculate_biorhythm(t, 23)  # fizyczna fala
emotional = calculate_biorhythm(t, 28)  # emocjonalna fala
intellectual = calculate_biorhythm(t, 33)  # intelektualna fala

print(f'Witaj {name}! Dzisiaj jest {t} dzień Twojego życia!')
print('Wyniki Twoich biorytmów prezentują się następująco:')
print(f'  Fizyczna fala: {physical:.4f}')
print(f'  Emocjonalna fala: {emotional:.4f}')
print(f'  Intelektualna fala: {intellectual:.4f}')

# obliczanie biorytmów na następny dzień
next_day_physical = calculate_biorhythm(t + 1, 23)
next_day_emotional = calculate_biorhythm(t + 1, 28)
next_day_intellectual = calculate_biorhythm(t + 1, 33)

if physical > 0.5 and emotional > 0.5 and intellectual > 0.5:
    print("Świetny wynik!")
elif physical < -0.5 or emotional < -0.5 or intellectual < -0.5:
    print('\nJutrzejsze biorytmy:')
    print(f'  Fizyczna fala: {next_day_physical:.4f}')
    print(f'  Emocjonalna fala: {next_day_emotional:.4f}')
    print(f'  Intelektualna fala: {next_day_intellectual:.4f}')
    if next_day_physical > physical or next_day_emotional > emotional or next_day_intellectual > intellectual:
        print("Nie martw się. Jutro będzie lepiej!")
    else:
        print(":(")