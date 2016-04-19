import hashmap

states = hashmap.new()
hashmap.set(states, "Galati", "GL")
hashmap.set(states, "Ilfov", "IF")
hashmap.set(states, "Alba", "AB")
hashmap.set(states, "Suceava", "SV")
hashmap.set(states, "Braila", "BR")

cities = hashmap.new()
hashmap.set(cities, "GL", "Galati")
hashmap.set(cities, "IF", "Bucuresti")
hashmap.set(cities, "AB", "Alba Iulia")
hashmap.set(cities, "SV", "Siret")
hashmap.set(cities, "BR", "Ianca")


print "-" * 10
print "GL State has: %s" % hashmap.get(cities, "GL")
print "BR State has: %s" % hashmap.get(cities, "BR")

print "-" * 10
print "Suceava has: %s" % hashmap.get(states,"Suceava")
print "Alba has: %s" % hashmap.get(states, "Alba")

print "-" * 10
hashmap.list(states)

print "-" * 10
hashmap.list(cities)

print "-" * 10
state = hashmap.get(states, "Satu Mare")

if not state:
    print "Sorry, no Satu Mare."

city = hashmap.get(cities, "SM", "Does Not Exist")
print "The city for the state 'SM' is: %s" % city
