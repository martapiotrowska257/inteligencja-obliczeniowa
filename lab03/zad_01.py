import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris1.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=291714)
# print(train_set)


# sortowanie po ostatniej kolumnie i kolejno sl, sw, pl, pw
train_set_sorted = sorted(train_set, key=lambda x: (x[4], x[3]))
train_set_sorted = pd.DataFrame(train_set_sorted, columns=df.columns)
# print(train_set_sorted.values)


def classify_iris(sl, sw, pl, pw):
    if 4.3 <= sl <= 5.8 and 2.9 <= sw <= 4.2 and 1.1 <= pl <= 1.9 and 0.1 <= pw <= 0.6:
        return "Setosa"
    elif 4.9 <= sl <= 7.0 and 2.0 <= sw <= 3.4 and 3.0 <= pl <= 5.1 and 1.0 <= pw <= 1.7:
        return "Versicolor"
    else:
        return "Virginica"


def prediction():
    good_predictions = 0
    length = test_set.shape[0]

    for i in range(length):
        if classify_iris(test_set[i, 0], test_set[i, 1], test_set[i, 2], test_set[i, 3]) == test_set[i, 4]:
            good_predictions += 1

    print(good_predictions)
    print(good_predictions / length * 100, "%")

    print(train_set)


prediction()  # 40 / 88.88888888888889 %

