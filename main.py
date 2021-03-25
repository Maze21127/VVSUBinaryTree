from node import *
from re import compile
import os
import time
import copy
import matplotlib.pyplot as plt


def check_inputs(list1):
    list_for_check = [str(s) for s in range(1, 11)]
    for elem in list1:
        if elem in list_for_check:
            return True


def do_magic(filename):
    global root, first_word
    try:
        start_count = copy.copy(root.count_words())
    except AttributeError:
        start_count = 0
    start_time = time.time()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            all_words = line.strip().split(' ')
            only_rus = [y for y in filter(r.match, all_words)]
            for word in sorted(only_rus):
                temp_check = True
                word = word.lower()
                if word[-1] in signs:
                    try:
                        if word[-3] == word[-2] == word[-1]:
                            word = word[:-3]
                            temp_check = False
                    except IndexError:
                        continue
                    if temp_check:
                        word = word[:-1]
                if '-' in word:
                    remove = word.split('-')
                    try:
                        for ww in remove:
                            root.insert(ww)
                    except AttributeError:
                        continue
                    continue
                if first_word:
                    root = Node(word)
                    first_word = False
                    continue
                root.insert(word)
        root.export_tree(output)
        temp_count = root.count_words()
        final_time = time.time() - start_time
        print('Поиск слов в ' + filename + ' завершен' + ' за ' + str(final_time)[:5] + ' секунд(-ы)')
        graph.append([final_time, temp_count-start_count])


signs = [',', '.', '!', '?', '-', ';', ':', '_', '«', '»', ')', '(', '…', '-']
r = compile("[а-яА-Я]+")
first_word = True
graph = list()
root = None

question = input('Искать во всех файлах? (y/номера файлов через запятую)\n')
answers = ['да', 'y']
check_input = True
files_list = list()
directory = os.getcwd()
output = os.getcwd()
output += '\\output.txt'

os.chdir(directory + '/files')
while check_input:
    if question in answers:
        files_list = list()
        for i in os.listdir(os.getcwd()):
            if os.path.splitext(i)[1] == '.txt':
                files_list.append(i)
        check_input = False
    else:
        input_list = list()
        numbers = question.split(',')
        numbers.sort()
        if check_inputs(numbers):
            for x in numbers:
                input_list.append(x + '.txt')
            for f in range(len(input_list)):
                if os.path.isfile(input_list[f]):
                    if input_list[f] not in files_list:
                        files_list.append(input_list[f])
                if f == len(input_list) - 1:
                    check_input = False
        else:
            question = input('Искать во всех файлах? (y/номера файлов через запятую)\n')

if os.path.getsize(output) > 0:
    open(output, 'w').close()

for txt in files_list:
    do_magic(txt)

list_time = list()
list_word = list()
for i in graph:
    list_time.append(i[0])
    list_word.append(i[1] // 1000)

# График
plt.bar(list_time, list_word)
plt.xlabel('Секунд')
plt.ylabel('Тысяч слов')
plt.title('Время')
plt.show()

if input('Найти слово?(да/y): ') in answers:
    find_word = input('Введите слово\n')
    search(root, find_word)
