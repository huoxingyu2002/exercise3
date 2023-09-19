import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt


file_path = "C:\\Users\\huoxingyu2020\\Desktop\\melville-moby_dick.txt"  
with open(file_path, "r") as file:
    text = file.read()


tokens = word_tokenize(text)


tagged = nltk.pos_tag(tokens)


fdist = FreqDist(tag for (word, tag) in tagged)


tags_freq = fdist.most_common()

tags = [tag for (tag, count) in tags_freq]
freqs = [count for (tag, count) in tags_freq]


plt.figure(figsize=(10, 6))
plt.bar(tags, freqs)
plt.xlabel(' parts of speech')
plt.ylabel('frequency')
plt.title('Frequency of occurrence of parts of speech')
plt.xticks(rotation=45)
plt.show()