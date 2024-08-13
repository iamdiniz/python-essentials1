user_word = str(input("Type your name: "))
user_word = user_word.upper()

# para cada letra em user word, faça...
for letter in user_word:
    if letter in "AEIOU":
        continue
    else:
        print(letter)
