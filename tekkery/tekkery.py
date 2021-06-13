import sys
from time import time

#считываем файл, текст подготовил. В первой строчке число слов, затем уже отдельные слова в каждой строчке
def readFile(file):
    with open(file, encoding="utf8") as f:
        size = int(f.readline().strip())
        lines = []
        for _ in range(size-1):
            lines.append(f.readline())
        return lines

# тест 1: обычная сортировка в лексикографическом порядке, в дельфи наверное так же будет
def sortWords(words):
    for i in range(0, len(words)-1):
        for j in range(i+1, len(words)):
            if (words[i] > words[j]):
                tmp = words[i]
                words[i] = words[j]
                words[j] = tmp

# тест 2: считаем колво встречающихся слов и потом их сортируем
def countWords(words):

    # создаем словарь, и складываем туда все слова
    dict = {}
    for word in words:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1

    keys = list(dict.keys())
    values = list(dict.values())

    # затем сортируем чтобы сначала были самые часто встречаемые
    for i in range(0, len(keys)-1):
        for j in range(i+1, len(keys)):
            if (values[i] < values[j]):
                tmp = values[i]
                values[i] = values[j]
                values[j] = tmp

                tmpK = keys[i]
                keys[i] = keys[j]
                keys[j] = tmpK

# самый первый тест один раз сортируем, для сортировки взял не весь текст иначе очень уж долго получалось
def sortOneTime():
    start =  int(time() * 1000)
    words = readFile("prep_text_part.txt")
    sortWords(words)
    end = int(time() * 1000)
    print(end - start)

# тут сортируем 10 раз выводим среднее время
def sortTenTime():
    start = int(time() * 1000)
    for i in range(0, 10):
        words = readFile("prep_text_part.txt")
        sortWords(words)
    end = int(time() * 1000)
    print((end - start)/10)

# здесь пересчитываем слова
def countOneTime():
    start =  int(time() * 1000)
    words = readFile("prep_text.txt")
    countWords(words)
    end = int(time() * 1000)
    print(end - start)


# sortOneTime()
countOneTime()