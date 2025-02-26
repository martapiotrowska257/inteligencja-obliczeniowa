# podpunkt a)

import datetime
import math

name = input('Jak się nazywasz? ')
year = input('Podaj rok urodzenia: ')
month = input('Podaj miesiąc urodzenia: ')
day = input('Podaj dzień urodzenia: ')

birthday = datetime.datetime(int(year), int(month), int(day))
todays_date = datetime.datetime.now()

t = (todays_date - birthday).days   # ilość dni życia od narodzin

# obliczanie biorytmów

physical = math.sin(((2 * math.pi) / 23) * t)   # fizyczna fala
emotional = math.sin(((2 * math.pi) / 28) * t)  # emocjonalna fala
intelectual = math.sin(((2*math.pi) / 33) * t)  # intelektualna fala

print(f'Witaj {name}! Dzisiaj jest {t} dzień Twojego życia!')
print(f'Wyniki Twoich biorytmów prezentują się następująco:'
      f'\n  fizyczna fala: {physical}'
      f'\n  emocjonalna fala: {emotional}'
      f'\n  intelektualna fala: {intelectual}')

# podpunkt b)

next_day_physical = math.sin(((2 * math.pi) / 23) * (t + 1))   # fizyczna fala
next_day_emotional = math.sin(((2 * math.pi) / 28) * (t + 1))  # emocjonalna fala
next_day_intelectual = math.sin(((2*math.pi) / 33) * (t + 1))  # intelektualna fala

if physical and emotional and intelectual > 0.5:
    print("Świetny wynik!")
elif physical or emotional or intelectual < -0.5:
    print(f'\n  jutrzejsza fizyczna fala: {next_day_physical}'
          f'\n  jutrzejsza emocjonalna fala: {next_day_emotional}'
          f'\n  jutrzejsza intelektualna fala:{next_day_intelectual}')
    if next_day_physical > physical or next_day_emotional > emotional or next_day_intelectual > intelectual:
        print("Nie martw się. Jutro będzie lepiej!")
    else:
        print(":(")

# podpunkt c)
# Spędziłam ok. 40 minut na zrobienie tego zadania, licząc czas łącznie z badaniami online.
