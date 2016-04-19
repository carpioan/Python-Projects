def product(list_num):
    total = 1
    for x in list_num:
        total *= x
    return total

print product([2,3,4,5,6,7,8])