import text2emotion as te

try:
    with open('pos_opinion.txt', 'r', encoding='utf-8') as file:
        pos_opinion = file.read()

    with open('neg_opinion.txt', 'r', encoding='utf-8') as file:
        neg_opinion = file.read()
except FileNotFoundError:
    print("Błąd: Nie znaleziono jednego lub obu plików.")

# Analiza emocji dla pozytywnej opinii
pos_emotions = te.get_emotion(pos_opinion)
# print(pos_emotions)

print("=== Analiza pozytywnej opinii ===")
print(f"Szczęście (Happy): {pos_emotions['Happy']:.3f}")
print(f"Złość (Angry): {pos_emotions['Angry']:.3f}")
print(f"Zaskoczenie (Surprise): {pos_emotions['Surprise']:.3f}")
print(f"Smutek (Sad): {pos_emotions['Sad']:.3f}")
print(f"Strach (Fear): {pos_emotions['Fear']:.3f}")
print()

# Analiza emocji dla negatywnej opinii
neg_emotions = te.get_emotion(neg_opinion)
# print(neg_emotions)

print("=== Analiza negatywnej opinii ===")
print(f"Szczęście (Happy): {neg_emotions['Happy']:.3f}")
print(f"Złość (Angry): {neg_emotions['Angry']:.3f}")
print(f"Zaskoczenie (Surprise): {neg_emotions['Surprise']:.3f}")
print(f"Smutek (Sad): {neg_emotions['Sad']:.3f}")
print(f"Strach (Fear): {neg_emotions['Fear']:.3f}")

