import datetime
import math


def get_user_birthdate():
    name = input('Jak się nazywasz? ')
    year = int(input('Podaj rok urodzenia: '))
    month = int(input('Podaj miesiąc urodzenia: '))
    day = int(input('Podaj dzień urodzenia: '))
    return name, datetime.datetime(year, month, day)


def calculate_biorhythm(days_lived, cycle_length):
    return math.sin(((2 * math.pi) / cycle_length) * days_lived)


def display_biorhythms(name, days_lived, physical, emotional, intellectual):
    print(f'Witaj {name}! Dzisiaj jest {days_lived} dzień Twojego życia!')
    print(f'Wyniki Twoich biorytmów prezentują się następująco: ')
    print(f'  Fizyczna fala: {physical: .4f}')
    print(f'  Emocjonalna fala: {emotional: .4f}')
    print(f'  Intelektualna fala: {intellectual: .4f}')


def check_next_day_biorhythms(t, physical, emotional, intellectual):
    next_physical = calculate_biorhythm(t + 1, 23)
    next_emotional = calculate_biorhythm(t + 1, 28)
    next_intellectual = calculate_biorhythm(t + 1, 33)

    if physical > 0.5 and emotional > 0.5 and intellectual > 0.5:
        print("Świetny wynik!")
    elif physical < -0.5 or emotional < -0.5 or intellectual < -0.5:
        print("\nJutrzejsze biorytmy:")
        print(f'  Fizyczna fala: {next_physical:.4f}')
        print(f'  Emocjonalna fala: {next_emotional:.4f}')
        print(f'  Intelektualna fala: {next_intellectual:.4f}')

        if next_physical > physical or next_emotional > emotional or next_intellectual > intellectual:
            print("Nie martw się. Jutro będzie lepiej!")
        else:
            print(":(")


def main():
    name, birthday = get_user_birthdate()
    todays_date = datetime.datetime.now()
    days_lived = (todays_date - birthday).days

    physical = calculate_biorhythm(days_lived, 23)
    emotional = calculate_biorhythm(days_lived, 28)
    intellectual = calculate_biorhythm(days_lived, 33)

    display_biorhythms(name, days_lived, physical, emotional, intellectual)
    check_next_day_biorhythms(days_lived, physical, emotional, intellectual)


if __name__ == "__main__":
    main()
