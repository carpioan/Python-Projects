class People(object):
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def preferences_fam(self):
        print self.name,
        print self.color,
        print self.age

my_name = People("John", "blue", 27)
wife_name = People("Christine", "green", 26)
first_child = People("Maria", "mov", 3)
second_child = People("Elisabeta", "yellow", 1)
print my_name.preferences_fam()
print wife_name.preferences_fam()
print first_child.name
