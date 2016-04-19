print """In timpul unui vis vezi doua case cu o arhitectura deosebita.
Casa #1 este veche, istorica, iar casa #2 este moderna. In care alegi sa intri?"""

casa = raw_input("> ")
if casa == "1":
	print """De cum intri in casa observi un living mare in mijlocul caruia se afla un pian.
In spatele pianului sunt doua usi. Alegi usa #1 sau usa #2?"""
	usa = raw_input("> ")
	if usa == "1":
		print """In spatele usii observi o camera in flacari. Pentru a stinge focul ai la dispozitie:
1. O vaza cu flori care mai are ceva apa in ea.
2. Un furtun pe care l-ai putea conecta la reteaua de apa.
3. O galeata cu apa murdara ramasa dupa ce femeia de serviciu a facut curatenie.
Ce alegi sa faci?"""
		fire = raw_input("> ")
		if fire == "1":
			print """Nu ti-a ajuns apa ca sa stingi focul. Poti:
1. Sa sari pe geam.
2. Sa te intorci pe usa pe care ai intrat."""
			escape = raw_input("> ")
			if escape == "1":
				print "Felicitari! Ai reusit sa scapi de flacari si sa chemi pompierii la timp."
			elif escape == "2":
				print "Din pacate nu ai mai putut iesi la timp din casa si ai fost salvat in ultima clipa de un pompier."
			else:
				print "Nu ai facut nicio alegere. Mai incearca!"
		elif fire == "2":
			print "Ai reusit sa stingi focul rapid. Proprietara iti ofera pianul drept recompensa."
			print """Ce vrei sa faci cu pianul?
1. Il iei acasa.
2. Il vinzi."""
			pian = raw_input("> ")
			if pian == "1":
				print """Desi este cam mare pentru casa ta, ai reusit sa-i gasesti loc pianului. 
Acum iei cursuri de pian."""
			elif pian == "2":
				print """Ai luat o suma frumusica pe pian intrucat avea o valoare istorica mare. 
Ai ales sa folosesti banii pentru a-ti renova casa."""
			else:
				print "Nu ai ales nimic. Replay!"
		elif fire == "3":
			print """Apa murdara continea agenti chimici care au intetit focul.
Pompierii au reusit sa stinga focul in ultimul moment.
Tu faci inchisoare pentru distrugere din culpa."""
		else:
			print "Nu ai ales nimic. Replay!"
	elif usa == "2":
		print """Cand intri in camera observi un laptop deschis si usa intredeschisa la baie.
Ce faci?
1. Verifici ce ar putea fi pe laptop.
2. Intri in baie sa vezi ce se intampla."""
		verificare = raw_input("> ")
		if verificare == "1":
			print "Laptopul este protejat cu parola. Alegi sa #1 spargi parola sau #2 renunti si pleci."
			alege = raw_input("> ")
			if alege == "1":
				print "Reusesti sa spargi parola si afli ca erai urmarit de un agent sub acoperire."
			elif alege == "2":
				print """Ajuns acasa incerci sa afli mai multe despre casa in care ai fost.
De fapt toate incercarile tale de a afla ceva s-au dovedit a fi in zadar. Toate dosarele erau secretizate."""
			else:
				print "Nu ai ales nimic. Replay!"
		elif verificare == "2":
			print """In baie esti intampinat de un agent sub acoperire care te anunta ca esti arestat.
Ti se pun catusele si esti dus la politie."""
		else:
			print "Nu ai ales nimic. Replay!"
	else:
		print "Nu ai ales nimic. Replay!"
elif casa == "2":
	print """Desi abia construita, cea de-a doua casa pare a fi parasita. 
Alegi sa mergi #1 in living sau #2 in dormitor."""
	livdor = raw_input("> ")
	if livdor == "1":
		print "In living este o valiza. #1 o deschizi sau #2 o iei cu tine?"
		valiza = raw_input("> ")
		if valiza == "1":
			print """Valiza este plina cu bani, dar inainte de a lua ceva esti prins de un agent sub acoperire.
Valiza este confiscata si tu primesti cateva luni de inchisoare cu suspendare."""
		elif valiza == "2":
			print """Odata ajuns acasa deschizi valiza si observi ca e plina cu bani.
Te hotarasti sa pleci din tara pentru totdeauna."""
		else:
			print "Nu ai ales nimic. Replay!"
	elif livdor == "2":
		print """ In dormitor nu gasesti decat cateva haine aruncate pe pat.
#1 le verifici sau #2 le lasi acolo si pleci?"""
		haine = raw_input("> ")
		if haine == "1":
			print "Gasesti documentele unui agent secret, dar esti prins inainte de a putea fugi."
		elif haine == "2":
			print """Ajungi acasa si incepi sa supraveghezi casa invecinata.
Nu dupa mult timp afli ca ea era folosita pe post de ascunzatoare de un agent secret."""
		else:
			print "Nu ai ales nimic. Replay!"
	else:
		print "Nu ai ales nimic. Replay!"
else:
	print "Te-ai trezit din vis inainte de a putea intra intr-o casa. Mai incearca!"