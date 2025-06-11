import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from collections import Counter
import wordcloud
from wordcloud import WordCloud

# nltk.download('all')
# nltk.download('stopwords')


# a) wczytanie artykułu z pliku article.txt i zamiana tekstu na małe litery
with open('article.txt', 'r', encoding='utf-8') as file:
    article = file.read().lower()

# b) Tokenizacja tekstu na zdania
sentences = nltk.sent_tokenize(article, language='english')     # lista zdań
print(f"Liczba zdań w artykule: {len(sentences)}")

# Tokenizacja zdań na słowa
list_of_lists = [nltk.word_tokenize(sentence, language='english') for sentence in sentences]    # lista list, w której każdy element (lista) zawiera tokeny (słowa) z jednego zdania
tokens = [token for sentence_tokens in list_of_lists for token in sentence_tokens]              # spłaszczona lista, zawierająca wszystkie słowa już w jednym miejscu
print(f"Liczba tokenów (słów): {len(tokens)}")

# c) Usunięcie stop words (słów nieznaczących) używając standardowej listy dla słów angielskich
stop_words = set(stopwords.words('english'))
tokens_without_stopwords = [token for token in tokens if token not in stop_words]
print(f"Liczba tokenów po usunięciu stop words: {len(tokens_without_stopwords)}")

# d) Usunięcie dodatkowych stop words, które dalej znajdują się w naszym zestawie słów (bag of words)
# print (tokens_without_stopwords)
additional_stop_words = ["'s", "n't", "'ve", "'re", ".", ",", ":", ";", "''", "\"\"", "``", "`", "(", ")", "[", "]",
                         "{", "}", "\\", "/", "?", "!", "-", ]
stop_words.update(additional_stop_words)
tokens_without_any_stopwords = [token for token in tokens if token not in stop_words]
print(f"Liczba tokenów po usunięciu dodatkowych stop words: {len(tokens_without_any_stopwords)}")

# e) Lematyzacja - proces sprowadzania słów do ich podstawowej formy słownikowej (tzw. lematu),
# z uwzględnieniem kontekstu i zasad gramatyki (np. "kupiłem" -> "kupić")
# Zdecydowałam się na wykorzystanie lematyzera nltk
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens_without_any_stopwords]
# print(lemmatized_tokens)
print(f"Liczba tokenów po dokonaniu lematyzacji: {len(lemmatized_tokens)}")

# --- Dla testu wykonałam także stemming ---

# Stemming - algorytmiczny proces usuwania końcówek fleksyjnych słów w celu uzyskania rdzenia,
# często bez uwzględnienia poprawności językowej (np. "kupiłem" -> "kup")
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens_without_any_stopwords]
# print(stemmed_tokens)
print(f"Liczba tokenów po dokonaniu stemmingu: {len(stemmed_tokens)}")


# f) Częstość występowania słów
word_freq = Counter(tokens_without_any_stopwords)
most_common_words = word_freq.most_common(10)
print("10 najczęściej występujących słów:")
for word, count in most_common_words:
    print(f"{word}: {count}")

# Wizualizacja - wykres słupkowy 10 najczęściej występujących słów
plt.figure(figsize=(12, 6))
words, counts = zip(*most_common_words)
plt.bar(words, counts)
plt.xlabel('Słowa')
plt.ylabel('Liczba wystąpień')
plt.title('10 najczęściej występujących słów w artykule')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('word_frequency.png')
plt.show()

# g) Chmura tagów (word cloud)
def wordCloud(tokens):
    wordcloud = WordCloud().generate(' '.join(tokens))
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud)
    plt.axis('off')

wordCloud(tokens_without_any_stopwords)
plt.savefig('word_cloud.png')
plt.show()