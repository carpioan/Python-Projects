
def remove_duplicates(list_num):
    total = []
    for num in list_num:
        if num not in total:
            total.append(num)
    return total

print remove_duplicates([2,3,4,5,2,3,4,5,2,3,4,5])


