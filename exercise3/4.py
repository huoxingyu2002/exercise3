import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


file_path = "C:\\Users\\huoxingyu2020\\Desktop\\melville-moby_dick.txt"  
with open(file_path, "r") as file:
    text = file.read()


tokens = word_tokenize(text)


tagged = nltk.pos_tag(tokens)


fdist = FreqDist(tag for (word, tag) in tagged)

top_tags = fdist.most_common(5)


for tag, count in top_tags:
    print(f"{tag}: {count}")