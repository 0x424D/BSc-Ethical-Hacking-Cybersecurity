print("----------121COM Week 2 Lab Exercise 7----------")
print("-------------Escape From Fukundo Bay------------")
print("------------------Aidan Redden------------------")
print("\n")

print("You awake in a dark room.  Do you:")
print("a) Scream for help.")
print("b) Press the light switch")
x = input("Enter a or b: ")
if x == "a":
	print("Someone hears your screams...")
	input()
	print("You hear chains jangle before a gruff voice emerges from the darkness about 10 feet to your right.")
	input()
	print("\"You too, huh?\"")
	input()
	print("As the mystery voice echoes and dissipates, you feel cold metal pressing against your arms.")
	input()
	print("You try to move them but they are restricted. You can feel the same cool restriction around your ankles.")
	input()
	print("Do you:")
	print("a) Ask the mystery voice where you are.")
	print("b) Ask the mystery voice who they are.")
	print("c) Say nothing and continue to struggle to get free.")
	x = input("> ")
	x = y.lower()
	
	if x == "a":
		print("You ask the voice where you are.")
		input()
		print("A long silence follows. You hear your companion sigh slowly before replying.")
		input()
		print("\"Kid, if I knew the answer to that question, I woulda started escaping already.\"")
		input()
		print("\"Ain't no point tryna escape if I don't know where to go afterwards.\"")
		input()
		print("You realise your acomplice has a southern drawl.")
		input()
	elif x == "b":
		pass
	elif x == "c":
		pass
	else:
		print("That was not an option. Game over.")

elif x == "b":
	print("The light comes on.")
	print("You do not recognise the room but you have a really bad feeling...")
	# Contine adventure Here
else:
	print("That was not an option.	Game Over")
