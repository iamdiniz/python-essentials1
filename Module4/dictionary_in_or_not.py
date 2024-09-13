dictionary = {
    "cat": "gato",
    "lion": "leão",
    "horse": "cavalo"
}

words = ["gato", "lion", "cavalo"]
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")