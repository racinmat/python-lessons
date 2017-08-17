# my python file
# from math import sin
# from functions import multiply_by_three
import glob
import json
from pathlib import Path

import pickle


def my_function(array):
    #     todo: implement
    # this function should multiply even numbers by two and divide odd numbers by two, and return array with modified numbers
    return []


def my_lambda(x):
    return x * 2


def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    # print(my_function(array))
    #
    #
    # for i in array:
    #     print("vypisuju")
    #     print(i)
    #
    # var = 3
    # if var / 3 == 1:
    #     print('je to 3')
    #
    #
    # new_arr = []
    # for i, j in enumerate(array):
    #     k = sin(0.3)
    #     new_arr.append(k)
    #
    # print(multiply_by_three(array))
    # val1 = 5
    # val2 = 4.6
    # print("hodnoty jsou " + str(val1) + " a " + str(val2))
    # print("hodnoty jsou {:d} a {:0.2f}".format(val1, val2))

    # i = 0
    # while True:
    #     x = int(input("zadej změnu\n"))
    #     i = (i + x) % 4
    #     print(i)

    # my_lambda = lambda x: x * 2
    # is_even = lambda x: x % 2 == 0
    # print(my_lambda(5))
    # print(is_even(5))
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(map(lambda x: x - 6, array))
    # print(list(map(lambda x: x - 6, array)))
    # print(list(map(lambda x: x > 4, array)))
    # print(list(filter(lambda x: not x % 2 == 0, array)))

    # print([x / 2 for x in my_array])
    # print([x for x in range(0, 15)])
    # print([x * 2 for x in range(0, 15)])
    # print([x for x in range(0, 15) if x < 10])
    # print([x * 2 for x in range(0, 15) if x < 10])

    # print(my_array[-1])
    # print(my_array[-3])
    # print(my_array[len(my_array) - 3])
    # colors = ['white', 'blue', 'yellow', 'red', 'green', 'orange', 'blue']
    # to_find = 'blue'
    # results = []
    # for key, x in enumerate(colors):
    #     if x == to_find:
    #         results.append(key)
    #         # break
    # print(results)
    #
    # file = open("file.txt", mode="r", encoding="utf8")      # pozor na encoding, když používám diakritiku
    # for line in file:
    #     print(line)
    # file.close()

    # with open("file.txt", mode="r", encoding="utf8") as file:
    #     for line in file:
    #         print(line)
    #
    # # print("tady už je soubor zavřený")
    #
    # with open("file_2.txt", mode="w", encoding="utf8") as file:
    #     file.write('nazdar\n')
    #     file.write('no nazdar')
    #
    # with open("file_2.txt", mode="a", encoding="utf8") as file:
    #     file.write('nazdar\n')
    #     file.write('no nazdar')

    # files = Path(".").glob('*/*.txt')
    # files = glob.glob('**/*.txt', recursive=True)
    # files = glob.glob('**', recursive=True)
    # print(files)
    # print(list(files))
    with open("config.json", mode="r", encoding="utf8") as file:
        data = json.load(file)
        # print(data)
        print(data['weapons'])

    class Animal:
        health = None
        name = None
        type = None

        def __init__(self, health, name, type) -> None:
            self.health = health
            self.name = name
            self.type = type


    def to_json(o):
        return o.__dict__

    my_pet = Animal(health=5, name='Macek', type='cat')

    my_data = {
        'level': 10,
        'name': 'Azathoth',
        'path_walked': [],
        'pet': my_pet
    }
    my_data['path_walked'].append('left')
    my_data['path_walked'].append('left')
    my_data['path_walked'].append('up')
    my_data['path_walked'].append('right')
    my_data['path_walked'].append('down')
    my_data['path_walked'].append('right')

    print(my_data)
    with open("saved_1.json", mode="w", encoding="utf8") as file:
        json.dump(my_data, file, indent=4, default=to_json)
    print("data saved")

    with open("saved_1.json", mode="r", encoding="utf8") as file:
        my_json_data_loaded = json.load(file)

    with open("file.dat", mode="wb") as file:
        pickle.dump(my_data, file)

    with open("file.dat", mode="rb") as file:
        my_data_loaded = pickle.load(file)

    print("hotovo")
