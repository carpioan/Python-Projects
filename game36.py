import random

pocket_list = []
table_phrase = "You put it in your pocket. "

def table_book():
	print "On table you find a knife and 2 books."

	choice_table = raw_input("What do you take?> ")
	compare_num = random.randint(1,2)

	if "knife" in choice_table:
		print "You taked the knife."
		pocket_list.append("knife_having")
		stairs()

	elif "book" in choice_table:

		if compare_num == 1:
			print "You taked a psihological book and started to read."
			pocket_list.append("psiho_book")
			stairs()

		elif compare_num == 2:
			print "You taked a book about fighting and read it."
			pocket_list.append("fight_book")
			stairs()

		else:
			print "You didn't pick anything."
			table_book()

	else:
		print "You didn't pick anything."
		table_book()


def win():
	win_list = ["You are so brave. Congratulations!", "You beat them so hard. Nice!", "You have serious injures, but you escaped.", "You almost got killed, but now you're free."]
	print win_list[random.randint(0,3)]

def dead():
	lose_list = ["You tried your best but you got killed.", "You aren't strong enough to beat them.", "You couldn't escape.", "Nice try, but you got killed!"]
	print lose_list[random.randint(0,3)]


def front_door():
	print "At the front door are 2 monsters."
	choice = raw_input("What do you do? >")
	if "open door" in choice and "fight_book" in pocket_list:
		win()
	else:
		dead()


def left_room():
	print "You open the door and find a warrior."
	left_room_choice = raw_input("What do you do? talk/fight> ")

	if "fight" in left_room_choice:
		if "knife_having" in pocket_list or "fight_book" in pocket_list:
			win()
		else:
			dead()

	elif "talk" in left_room_choice:
		if "psiho_book" in pocket_list:
			print "You tell him that you just search someone to talk with. He's glad that he can speak with you."
			print "The warrior talks about his drama. He was kidnapped when he was a little boy and was trained to kill."
			print "You try to understand him and to offer support. He's grateful to you because you helped him to talk about his drama."
			print "You tell him that you also have been kidnapped and you want to escape."
			warrior_choice = raw_input("You tell him 1.'Goodbye' or 2.'Come with me and became free!'?> ")

			if "1" in warrior_choice:
				print "You were so excited about warrior's drama that you jumped out the window."
				dead()

			elif "2" in warrior_choice:
				print "Warrior helped you to beat the monsters and he got free. You became his best friend."
				win()

			else:
				print "Learn to tape a number!"
				left_room()

		else:
			print "He didn't want to listen to you."

	else:
		print "You didn't choose anything."
		left_room()


def right_room():
	print "Here you find a little boy, a weapon and some clothes."
	right_room_choice = raw_input("What do you choose?> ")

	if "little boy" in right_room_choice:
		if "psiho_book" in pocket_list:
			print "You go to the little boy and try to talk with him. He explains to you that he was kiddnaped and he doesn't know where he is."
			print "You take the boy with you, smash the window and escape the house."
			win()

		elif "fight_book" in pocket_list:
			print "You take the little boy and teach him to fight."
			print "After that you go downstairs at the front door and fight the monsters."
			win()
		elif "knife" in pocket_list:
			print "You take the boy and smash the window."
			print "The monsters see you and you must fight them and defeat the boy."
			rand_num = random.randint(0,1)
			if rand_num == 1:
				win()
			else:
				dead()
		else:
			print "You try to talk with the boy, but he didn't listen to you."
			print "He taked the weapon and shout you."
			dead()

	elif "weapon" in right_room_choice:
		print "You take the boy and the weapon, go at the front door and try to kill the monsters."
		print "But the weapon wasn't charged and you and the boy got killed."
		dead()

	elif "clothes" in right_room_choice:
		print "You take the clothes and change."
		print "You put the boy on window, go downstairs, pass through monsters and take the boy from the window."
		win()

	else:
		print "You didn't tape anything"
		right_room()


def stairs():
	stairs_phrase = "Now you climb up the stairs and in front of your eyes you have two rooms: one to the left and one to the right."
	if "knife_having" in pocket_list or "fight_book" in pocket_list or "psiho_book" in pocket_list:
		print table_phrase + stairs_phrase
	else:
		print stairs_phrase

	choice_stairs = raw_input("Which room do you enter?> ")
	if "left" in choice_stairs:
		left_room()
	elif "right" in choice_stairs:
		right_room()
	else:
		print "You didn't choose anything."
		stairs()


def corridor():
	print "In corridor you see some stairs and a table."
	choice_corridor = raw_input("Do you go at the table or check the stairs?")

	if "table" in choice_corridor:
		table_book()
	elif "stairs" in choice_corridor:
		stairs()
	else:
		print "You didn't choose anything."
		corridor()


def start():
	print "You are a prisoner in a abandoned house."
	print "You must escape but at the front door of the house there are 2 monsters which you can't beat them without help."
	print "You have the chance to try to fight them or to find another way out."
	print "After you get out your room you see a corridor and the front door."
	first_choice = raw_input("What do you do?> ")
	if "front door" in first_choice:
		front_door()
	elif "corridor" in first_choice:
		corridor()
	else:
		print "You didn't choose anything."
		start()

start()