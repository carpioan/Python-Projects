class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Contrusctor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

milley_deep = Child("Deep", "green", 12)
Johnny_Deep = Parent("Deep", "green")
#print(milley_deep.last_name)
print(milley_deep.number_of_toys)
