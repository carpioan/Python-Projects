grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += ((score - average)**2)/len(scores)
    return variance
print grades_variance(grades)

var = grades_variance(grades)
def grades_std_deviation(var):
    return var**0.5
print grades_std_deviation(var)

print "The grades are: ", print_grades(grades)
print "The sum of the grades is: ", grades_sum(grades)
print "The average of the grades is: ", grades_average(grades)
print "The variance of the grades is: ", grades_variance(grades)
print "The standard deviation of grades is: ", grades_std_deviation(var)