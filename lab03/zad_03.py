import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, export_text

df = pd.read_csv("iris1.csv")
# a
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=291714)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]


# DD
def DD():
    model = DecisionTreeClassifier()
    model.fit(train_inputs, train_classes)
    y_pred_dd = model.predict(test_inputs)
    accuracy = model.score(test_inputs, test_classes)
    procent_dd = accuracy * 100
    print(f"Drzewo Decyzyjne - Dokładność: {procent_dd:.2f}%")
    cm = confusion_matrix(test_classes, y_pred_dd)
    print(cm)
    print("\n")


DD()

# KNN
k = [3, 5, 11]


def KNN(k):
    for i in k:
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(train_inputs, train_classes)
        y_pred_knn = knn.predict(test_inputs)
        accuracy = knn.score(test_inputs, test_classes)
        procent_knn = accuracy * 100
        print(f"k-NN (k={i}) - Dokładność: {procent_knn:.2f}%")
        cm = confusion_matrix(test_classes, y_pred_knn)
        print(cm)
        print("\n")


KNN(k)


# Naive Bayes
def NB():
    nb = GaussianNB()
    nb.fit(train_inputs, train_classes)
    y_pred_nb = nb.predict(test_inputs)
    accuracy_nb = accuracy_score(test_classes, y_pred_nb)
    procent_nb = accuracy_nb * 100
    print(f"Naive Bayes - Dokładność: {procent_nb:.2f}%")
    cm = confusion_matrix(test_classes, y_pred_nb)
    print(cm)


NB()

# najlepszy wynik otrzymano dla KNN gdzie k = 11 i wynosi on 100%
