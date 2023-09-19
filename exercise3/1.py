import re

def tokenize_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        tokens = re.findall(r'\b\w+\b', content)
        return tokens

file_path = 'melville-moby_dick.txt'
tokens = tokenize_file(file_path)
print(tokens)