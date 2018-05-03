print("Введите слово")
word = input()
word.split(' ')
print(word)
vowels = set("аеоуиыюяaeiouy")
fail = (' ', ',')
word_set = set(word.lower())
letter = 0
new_line = ''
for i in word:
    if i not in fail:
        print(sum(letter in vowels for letter in i))
print(sum(letter in vowels for letter in word))
