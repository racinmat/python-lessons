# my python file
# from math import sin
# from functions import multiply_by_three


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
    print([x for x in range(0, 15)])
    print([x * 2 for x in range(0, 15)])
    print([x for x in range(0, 15) if x < 10])
    print([x * 2 for x in range(0, 15) if x < 10])

