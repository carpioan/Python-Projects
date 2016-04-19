print "Acest test psihologic iti va spune cat de bine te poti concentra asupra unui lucru.\nRaspunde la fiecare intrebare au A(adevarat) sau F(fals).\nEsti pregatit? da/nu"

pregatit = raw_input("> ")

if pregatit == "da":
	print "Sa incepem."

else:
	print "Te astept sa revii oricand vrei."

score = 0
	
print "Ma bucur ca te-ai hotarat sa faci acest test."

print "1. Pot sa ma cocentrez intr-un mediu galagios."
int_1 = raw_input("> ")
if int_1 == "A":
	score += 1
else:
	score

print """2. Cand ma aflu intr-o situatie in care se intampla mute lucruri
si exista un volum mare de stimulare senzoriala, 
ca de exemplu la o petrecere sau in multime pe aeroport, 
potsa ma abtin sa ma pierd intr-un sir de ganduri 
despre vreunul din lucrurile pe care le vad."""
int_2 = raw_input("> ")
if int_2 == "A":
	score += 1
else:
	score
		
print """3. Daca ma hotarasc sa imi concentrez atentia asupra unei anumite sarcini, 
constat ca, de obicei, pot sa fac asta."""
int_3 = raw_input("> ")
if int_3 == "A":
	score += 1
else:
	score
	
print """4. Daca sunt acasa si incerc sa lucrez, sonorul televizorului 
sau zgomotele pe care le fac alte persoane\nma distrag foarte mult."""
int_4 = raw_input("> ")
if int_4 == "F":
	score += 1
else:
	score
	
print """5. Descopar ca daca stau linistit chiar si pentru cateva momente, 
un val de ganduri imi umple mintea si ma trezescu urmand siruri multiple 
de ganduri, deseori fara sa stiu cum a inceput fiecare in parte."""
int_5 = raw_input("> ")
if int_5 == "F":
	score += 1
else:
	score

print """6. Daca sunt distras de vreun eveniment neasteptat, 
pot sa imi reconcentrez atentia asupra a ceea ce faceam."""
int_6 = raw_input("> ")
if int_6 == "A":
	score += 1
else:
	score

print """7. In cursul unor perioade de liniste relativa, de exemplu
atunci cand sunt in autobuz sau tren ori astept la coada la un magazin,
remarc o multime de lucruri impreurul meu."""
int_7 = raw_input("> ")
if int_7 == "A":
	score += 1
else:
	score

print """8. Atunci cand un proiect individual are nevoie de intreaga mea atentie si concentrare,
incerc sa lucrez in cel mai linistit loc pe care il gasesc."""
int_8 = raw_input("> ")
if int_8 == "F":
	score += 1
else:
	score

print """9. Atentie mea tinde sa fie captivata de stimuli  si de evenimente 
din mediul inconjurator si imi este greu sa le ignor odata ce se intampla acest lucru."""
int_9 = raw_input("> ")
if int_9 == "F":
	score += 1
else:
	score
	
print """10. Imi este usor sa stau de vorba cu cineva intr-o atmosfera aglomerata,
de exemplu la un cocktail sau intr-un birou aflat intr-un spatiu deschis; 
pot sa ii ignor pe cei din jur, cu care nu dialoghez, 
sau pot distinge ceea ce spun daca ma concentrez.""" 
int_10 = raw_input("> ")
if int_10 == "A":
	score += 1
else:
	score

if score > 7:
	print "Felicitari! Te situezi la capatul Concentrat al dimensiunii atentiei. Ai un scor de %s puncte." % score
elif score <= 3:
	print "Din pacate tinzi sa fii Neatent. Lucreaza un pic cu atentia ta. Ai un scor de %s puncte." % score
else:
	print """Nu e rau!
Te situezi intre cele doua capete ale dimensiuni atentiei cu un scor de %s puncte.
Daca vrei sa-ti imbunatatesti atentia fa cateva exercitii in acest sens.""" % score