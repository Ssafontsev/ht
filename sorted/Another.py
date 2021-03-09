import operator
from pprint import pprint
import os

def get_info(file_names):
    my_data = {}
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            my_data.update({file: f.readlines()})
    my_data_len = {key: len(value) for key, value in my_data.items()}

    sorted_key_list = sorted(my_data_len.items(), key=operator.itemgetter(1))

    my_data = [{item[0]: my_data[item[0]]} for item in sorted_key_list]
    pprint(my_data)

    return my_data



def writing_to_file(my_data, my_file):
    with open(my_file, 'w', encoding='utf-8') as f:
        for file in my_data:
            for key, value in file.items():
                f.write(key + '\n')
                f.write(str(len(value)) + '\n')
                for elem in value:
                    f.write(elem.strip() + '\n')
                    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

writing_to_file(get_info(['1.txt', '2.txt', '3.txt']), 'result.txt')

  # Вариант решения с использованием списка
# def get_info(file_names):
#
#     my_data = []
#     for file in file_names:
#         with open(file, encoding='utf-8') as f:
#             lines = f.read().splitlines()
#             my_data.append([file, len(lines)])
#             my_data[len(my_data)-1] += lines
#
#     my_data.sort(key=len)
#     return my_data
#
# def writing_to_file(my_data, my_file):
#
#     with open('result.txt', 'w', encoding='utf-8') as f:
#         for file in my_data:
#             for elem in file:
#                 print(elem)
#
#                 f.write(f'{elem}\n')
#     file_path = os.path.join(os.getcwd(), my_file)
#     print(file_path)
#
#     return file_path
#
# print(writing_to_file(get_info(['1.txt', '2.txt', '3.txt']), 'result.txt'))
