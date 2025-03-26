import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

df = pd.read_csv("iris1.csv")

# podpunkt a)
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=291714)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# print(train_set)
# print(test_set)

# podpunkt b)
model = DecisionTreeClassifier()

# podpunkt c)
model.fit(train_inputs, train_classes)


# podpunkt d)
def drzewo_text():
    tree_text = export_text(model, feature_names=list(df.columns[:-1]))  # pomijamy kolumnę z etykietami
    print(tree_text)


drzewo_text()

# podpunkt e)
prediction = model.predict(test_inputs)
accuracy = model.score(test_inputs, test_classes)

print(prediction)
print(accuracy)  # przykładowe wyniki: 0.9555555555555556, 0.9333333333333333

# podpunkt f)
cm = confusion_matrix(test_classes, prediction)
print(cm)


def wykres():
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
    plt.xlabel("Przewidywane")
    plt.ylabel("Rzeczywiste")
    plt.title("Macierz błędów")
    plt.show()


wykres()

# AI okazało się lepsze od człowieka, jednak nieznacznie
# accuracy kodu napisanego przeze mnie: 88.88888888888889 %
# accuracy kodu napisanego przez AI: ok. 0.9333333333333333 - 0.9555555555555556
