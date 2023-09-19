import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


with open('melville-moby_dick.txt', 'r') as file:
    data = file.read()


tokens = nltk.word_tokenize(data)


stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]


top_20_tokens = filtered_tokens[:20]


lemmatized_tokens = [lemmatizer.lemmatize(token) for token in top_20_tokens]

print(lemmatized_tokens)