people = 45
cars = 35
trucks = 40


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks and trucks > cars:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

a = raw_input(int("Valoarea lui a este:"))
b = raw_input(int("Valoarea lui b este:"))
if 