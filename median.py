def median(list_num):
    list_num.sort()
    for i in list_num:
        if len(list_num) % 2 == 0:
            first_num = len(list_num) / 2
            second_num = len(list_num) / 2 - 1
            total = list_num[first_num] + list_num[second_num]
            final_num = total / 2.0
            return final_num
        elif len(list_num) < 2:
            print list_num[len(list_num)-1]
        else:
            final_num = list_num[len(list_num) / 2]
            return final_num

print median([5,3,1])
