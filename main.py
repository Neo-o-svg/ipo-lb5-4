# Сформируйте новую строку, состоящую из первых букв каждого слова, введенного пользователем.


# создаем переменную и присваиваем ей строку, введенную пользователем
string = input("Введите строку: ").lower()


# создаем список из слов строки
list_of_words = string.split()


# создаем список из первых букв каждого слова
first_letters = [
    word[0] for word in list_of_words
]
# склеиваем все элементы списка в строку
new_string = ''.join(first_letters)


# выводим строку
print(new_string)


