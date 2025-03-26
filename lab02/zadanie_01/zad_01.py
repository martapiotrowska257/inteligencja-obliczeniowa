import pandas as pd
import numpy as np

df = pd.read_csv(
    "c:\\Marta\\Studia\\semestr_4\\inteligencja_obliczeniowa\\inteligencja-obliczeniowa\\lab02\\zadanie_01"
    "\\iris_with_errors.csv"
)

# print(df.values)

df.replace("-", np.nan, inplace=True)

if 'species' not in df.columns and 'variety' in df.columns:
    df.rename(columns={'variety': 'species'}, inplace=True)


# podpunkt a - sprawdzenie brakujących danych
def missing_data_details(df):
    missing_values = df.isnull().sum()
    total_missing = missing_values.sum()
    print(f"\nBrakujące wartości w kolumnach:\n{missing_values}")
    print(f"\nŁączna liczba brakujących wartości: {total_missing}")
    return total_missing


missing_data_details(df)


# podpunkt b - poprawa danych numerycznych
def fix_numerical_data(df, min_val=0, max_val=15):
    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].apply(lambda x: np.nan if x < min_val or x > max_val else x)
        df[col] = df[col].fillna(df[col].median())


fix_numerical_data(df)


# podpunkt c - poprawa nazw gatunków
def fix_species_names(df):
    if 'species' in df.columns:
        valid_species = {"Setosa": "Setosa", "Versicolor": "Versicolor", "Virginica": "Virginica"}
        df["species"] = df["species"].str.strip().map(valid_species).fillna("Nieznany")


fix_species_names(df)

# zapis poprawionych danych
df.to_csv("iris_cleaned.csv", index=False)

df_cleaned = pd.read_csv("iris_cleaned.csv")
print(df_cleaned.values)
