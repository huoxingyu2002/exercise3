def filter_stopwords(file_path):
    stopwords = ['the', 'a', 'an', 'is', 'in']

    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = content.split()

        filtered_words = [word for word in words if word not in stopwords]

        return filtered_words


file_path = 'melville-moby_dick.txt'
filtered_words = filter_stopwords(file_path)
print(filtered_words)