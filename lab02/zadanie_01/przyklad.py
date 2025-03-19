import pandas as pd

df = pd.read_csv("iris1.csv")

# print(df)
print(df.values)

# wszystkie wiersze, kolumna nr 0
# print(df.values[:, 0])

# wiersze od 5 do 10, wszystkie kolumny
# print(df.values[5:11, :])

# dane w komórce [1,4]
# print(df.values[1, 4])
