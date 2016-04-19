import random

count = 0
armour = ["head", "legs", "abdomen", "arm"]
your_score = 0
monster_score = 0
condition1 = False

monster_hit = armour[random.randint(0, len(armour)-1)]
your_defense = raw_input("What do you defense?\n%s> " % '/'.join(armour))

def your_turn():
    print "Your turn."
    monster_defense = armour[random.randint(0, len(armour)-1)]
    your_hit = raw_input("Choose where to hit.\n%s> " % '/'.join(armour))

def monster_turn():
    print "Monster turn."
    monster_hit = armour[random.randint(0, len(armour)-1)]
    your_defense = raw_input("What do you defense?\nhead/legs/abdomen/arm")

def play():



while count != 5:
    if monster_defense != your_hit:
        print "You hit him."
        your_score += 1
    elif monster_defense == your_hit:
        count += 1
        print "Your hit has been defetead."
        if monster_hit != your_defense:
            print "He hit you."
            monster_score += 1
    else:
        print "You defeated his hit."
        count += 1

    """if monster_defense == your_hit:
        print "Your hit has been defeated."
        return monster_turn()
    else:
        print "You hit him."
        return your_turn()"""



    if monster_hit == your_defense:
        print "You defended yourself."
        return your_turn()
    else:
        print "You've been hurted."
        return monster_turn()


"""import time
import random

quips = [
        "You have been killed.",
        "Maybe will have more luck next time.",
        "RIP.",
        "You aren't so good at that.",
        "You didn't do it so well."
    ]

for i in quips[random.randint(0, len(quips)-1)]:
    print i,
    time.sleep(0.1)
#while count != 6:"""

        
