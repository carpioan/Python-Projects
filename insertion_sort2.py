import timeit
import random

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped



data_list = [x for x in range(1, 10000)]


def insertion_sort(to_sort_list):
    a = 1

    while a <= len(to_sort_list) - 1:
        img_num = to_sort_list[a]
        b = a - 1

        while b >= 0 and to_sort_list[b] > img_num:
            to_sort_list[b + 1] = to_sort_list[b]
            b = b - 1

        to_sort_list[b + 1] = img_num
        a = a + 1

#wrapped2 = wrapper(insertion_sort, data_list)
#print(timeit.timeit(wrapped2, number=1))
print(data_list)


