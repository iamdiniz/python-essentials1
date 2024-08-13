word_without_vowels = ""
user_word = str(input("Type your name: "))
user_word = user_word.upper()

# para cada letra em user word, faça...
for letter in user_word:
    if letter in "AEIOU": # se na variavel letra tiver algumas dessas...
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)
