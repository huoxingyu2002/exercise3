import nltk
nltk.download('punkt')

def pos_tagging(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        tokens = nltk.word_tokenize(content)
        tagged_words = nltk.pos_tag(tokens)

        return tagged_words

file_path = 'melville-moby_dick.txt'
tagged_words = pos_tagging(file_path)
print(tagged_words)