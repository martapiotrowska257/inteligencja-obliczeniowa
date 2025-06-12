import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

# nltk.download('vader_lexicon')

sentiment_analyzer = SentimentIntensityAnalyzer()

try:
    with open('pos_opinion.txt', 'r', encoding='utf-8') as file:
        pos_opinion = file.read()

    with open('neg_opinion.txt', 'r', encoding='utf-8') as file:
        neg_opinion = file.read()
except FileNotFoundError:
    print("Błąd: Nie znaleziono jednego lub obu plików.")


# Analiza sentymentu dla pozytywnej opinii
pos_scores = sentiment_analyzer.polarity_scores(pos_opinion)

print("=== Analiza pozytywnej opinii ===")
print(f"Pozytywny (pos): {pos_scores['pos']:.3f}")
print(f"Negatywny (neg): {pos_scores['neg']:.3f}")
print(f"Neutralny (neu): {pos_scores['neu']:.3f}")
print(f"Zagregowany wynik (compound): {pos_scores['compound']:.3f}")
print()

# Analiza sentymentu dla negatywnej opinii
neg_scores = sentiment_analyzer.polarity_scores(neg_opinion)

print("=== Analiza negatywnej opinii ===")
print(f"Pozytywny (pos): {neg_scores['pos']:.3f}")
print(f"Negatywny (neg): {neg_scores['neg']:.3f}")
print(f"Neutralny (neu): {neg_scores['neu']:.3f}")
print(f"Zagregowany wynik (compound): {neg_scores['compound']:.3f}")
