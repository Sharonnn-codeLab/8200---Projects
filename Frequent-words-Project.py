import sys
import string

filename = input(r"Enter the file name, full path recommended: ").strip('"')
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

text = text.translate(str.maketrans("","", string.punctuation))

text = text.lower()

list_words = text.split()

dict_words = {}
for word in list_words:
    if word in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1

sorted_words = sorted(dict_words.items(), key=lambda x:x[1], reverse=True)

N = int(sys.argv[1])
try:
    if (N > 0):
        for idx, (word, count) in enumerate(sorted_words[:N], start = 1):
            print(f"{idx}.word - '{word}', times - '{count}'")
except ValueError:
        print("Please enter a positive integer argument")

