# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
# Решение
# size= int(input("Введите размер массива: "))
# from random import randint
# list1=[randint(1,10) for i in range(size)]
# number= int(input("Введите искомое число: "))
# count=0
# for i in range(len(list1)):
#     if(list1[i]==number):
#         count=count+1

# print(list1)
# print(count)





# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
# Решение
# size= int(input("Введите размер массива: "))
# from random import randint
# list1=[randint(1,10) for i in range(size)]
# number= int(input("Введите искомое число: "))
# min=list1[0]
# for i in range(len(list1)):
#     if (abs(number-list1[i])<abs(number-min)):
#         min=list1[i]
# print(list1)
# print(number)
# print(f"->{min}")



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Решение

# d=dict()
# d=[{1:"AEIOULNSTR"},{2:"DG"},{3:"BCMP"},{4:"FHVWY"},{5:"K"},{8:"JX"},{10:"QZ"},{1:"АВЕИНОРСТ"},{2:"ДКЛМПУ"},{3:"БГЁЬЯ"},{4:"ЙЫ"},{5:"ЖЗХЦЧ"},{8:"ШЭЮ"},{10:"ФЩЪ"}]
# word=list(input("Введите слово: "))
# word=[x.upper() for x in word]
# count=0
# for i in word:
#         for p in d:
#             for j in p:
#                 for m in p[j]:
#                     if i==m:
#                         count=count+j
# print(count)


# Вариант 2

# list1=list(input("Введите слова на русском или на латинском языке с : "))
# list2=[x.upper() for x in list1]
# print(list1)
# count=0
# for  i in list2:
#     if i== "A"or i=="E"or i== "I"or i== "O"or i== "U"or i== "L"or i== "N"or i== "S"or i== "T"or i== "R"or i=="А"or i== "В"or i== "Е"or i== "И"or i== "Н"or i== "О"or i== "Р"or i== "С"or i== "Т":
#         count=count+1
#     if i== "D"or i== "G" or i== "Д"or i== "К"or i=="Л"or i=="М"or i== "П"or i== "У":
#         count=count+2
#     if i== "B" or i=="C"or i=="M"or i=="P"or i=="Б"or i== "Г"or i== "Ё"or i== "Ь"or i== "Я":
#         count=count+3
#     if i== "F"or i== "H" or i== "V" or  i=="W" or i=="Y"or i=="Й"or i== "Ы":
#         count=count+4
#     if i== "J"or i== "X"or i=="Ш"or i== "Э"or i== "Ю":
#         count=count+8
#     if i== "K"or i=="Ж"or i== "З"or i== "Х"or i== "Ц"or i== "Ч":
#         count=count+5
#     if i== "Q"or i== "Z"or i=="Ф"or i== "Щ"or i== "Ъ":
#         count=count+10 

    
# print(count)



# *Пример:*
# ноутбук
#     12