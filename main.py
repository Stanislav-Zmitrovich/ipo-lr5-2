# Запрашиваем у пользователя две строки
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

# Приводим строки к нижнему регистру и удаляем пробелы (если необходимо)
str1 = str1.lower().replace(" ", "")
str2 = str2.lower().replace(" ", "")

# Инициализируем два словаря для подсчета количества символов
char_count1 = {}
char_count2 = {}

# Подсчитываем количество каждого символа в первой строке
for char in str1:
    if char in char_count1:
        char_count1[char] += 1
    else:
        char_count1[char] = 1

# Подсчитываем количество каждого символа во второй строке
for char in str2:
    if char in char_count2:
        char_count2[char] += 1
    else:
        char_count2[char] = 1

# Проверяем, равны ли словари
is_anagram = char_count1 == char_count2

# Выводим результат
if is_anagram:
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")
