
def purify(list_num):
    odd_num = []
    for num in list_num:
        if num % 2 == 1:
            odd_num.append(num)
    return odd_num

print purify([1,2,3,4,5,6,7,8,9,11])


