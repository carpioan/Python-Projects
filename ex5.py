name = 'Zed A. Shaw'
age = 35
height = 74
height_cm = height * 2.54
weight = 180
weight_kg = weight * 0.453
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d tall in centimeters." % height_cm
print "He's %d pounds heavy." % weight
print "In kilograms he's %d heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "If I add %d, %d, and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg)