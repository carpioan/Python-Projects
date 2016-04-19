def CheckNums(num):
    hours = num / 60
    minute = num % 60
    if num < 60:
        return "0:%s" %num
    elif num >= 60:
        return "%s:%s" % (hours, minute)

print CheckNums(64)