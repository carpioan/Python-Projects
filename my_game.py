class Person:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name, age, job):
        """Initializes the data."""
        self.name = name
        self.age = age
        self.job = job
        print("(Presenting yourself {})".format(self.name))

        # When this person is created, the person
        # adds to the population
        Person.population += 1

    def die(self):
        """I am dying."""
        print("{} is dying!".format(self.name))

        Person.population -= 1

        if Person.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} persons working.".format(
                Person.population))

    def say_hi(self):
        """Greeting by the person.

        Yeah, they can do that."""
        print("Greetings, my name is {}, I'm {} years old and I'm working as {}.".format(self.name, self.age, self.job))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} persons.".format(cls.population))

person1 = Person("John", 37, "freelancer")
person1.say_hi()
Person.how_many()

person2 = Person("Eve", 27, "economist")
person2.say_hi()
Person.how_many()

person3 = Person("Michael", 32, "professor")
person3.say_hi()
person3.how_many()

print("\nPersons can do some work here.\n")

print("Persons have finished their work. So let's wait them to die.")
person1.die()
person2.die()
person3.die()

Person.how_many()