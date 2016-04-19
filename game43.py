from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You have been killed.",
        "Maybe will have more luck next time.",
        "RIP.",
        "You aren't so good at that.",
        "You didn't do it so well."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Shore(Scene):

    def enter(self):
        print "The ship full of people was wreck on. Some of survivors are on an island,"
        print "but it seems that the island is full of cannibals. You must do something"
        print "to rescue that people and you decide to go there. You take a boat and some"
        print "food and navigate to the island. A friend gives you a map of island."
        print "You are now on the island shore and you have been searching for 3 hours but "
        print "you didn't find anything. You must try something else. You see the forest, a car and a cave."

        action = raw_input("forest, car or cave?> ")

        if action == "car":
            print "You go to the car. You can't find the keys."
            print "You decide to break the wires of contact keys and try to start the car's engine."
            print "In the car was placed a bomb and the car exploded."
            return "death"

        elif action == "forest":
            print "You enter the forest and a cannibal come across."
            print "You decide to fight him."
            armour = random.randint(0,4)
            fight = raw_input("Choose where to hit. head/legs/abdomen/hand> ")
            print "After the forest you find the cannibals village."
            print "You decide to go "


            action2 = raw_input("go back, talk to man or burn the village?")
            if action2 == "go back":
                print "You didn't succeed to save the people. You lose."
                exit(1)
            elif action2 == "talk to man":
                print ""

