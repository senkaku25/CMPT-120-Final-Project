####-----------------------FUNCTIONS-------------------------###
def txttolist():
	useFile = input("Would you like to upload a custom map (write in file with .txt) or use the default(d) ?	")
	
	if useFile == "d" :
		useFile = "planets.txt"
	
	fileRef = open(useFile,"r") # opening file to be read
	localList=[]

	for line in fileRef:
		string = line[0:len(line)-1]  # eliminates trailing '\n'
									# of each line 
		localList.append(string)  # adds string to list

	fileRef.close()
	#print(localList)
	return(localList)
	##Use localList to access planets


def presentlist(putinList,moves): ##presents list of planets to player so they can see map
	print("Here is your map: ")
	print("Planet", "Civ-Level", "Fuel", "Rocks :^)")

	y = ""
	newPlist = []
	for r in range(len(putinList)):
		spaces = "     "
		x = ""
		m = putinList[r]
		for i in range(len(m)):
			x = x+str(m[i])
		newPlist.append(x)
		gr8 = str(r)
		if moves == r:
			y = y+gr8+spaces+x+"   <=== Astronaut :)"+"\n"
		else:
			y =y+gr8+spaces+x+"\n"
	print(y)
	#print(newPlist)
	return newPlist


def mildexplode(currentList):
	lenny = len(currentList)*5
	donefor = random.randint(1,lenny)
	if donefor >= len(currentList):
		print("Mild explosion happened in a galaxy far away!!")
		return currentList
	else:
		## del currentList[donefor] <-- use for mega!!!
		for r in range(1,donefor):
			effected = currentList[r]
			newinfo = ""
			oldrocks = 0
			if effected[-2].isdigit():
				for i in range(len(effected)-2):
					newinfo = newinfo + effected[i]
				oldrocks = int(effected[-1])+(10*int(effected[-2]))
			else:
				for i in range(len(effected)-1):
					newinfo = newinfo + effected[i]
				oldrocks = int(effected[-1])
			newinfo = newinfo+str(oldrocks+r*10)
			currentList[r] = newinfo
		#print(currentList)
	print("Wowzer, a mild explosion happened in planet:",donefor)
	return currentList


def AMAZINGEXPLODEXD(currentList,posi):
	lenny = len(currentList)*5
	donefor = random.randint(1,lenny)
	if posi == donefor:
		print("OH NO!! You got caught in a BIG AMAZING explosion!!! you died because it was so big!")
		return -1 ##kills player
	if donefor >= len(currentList): #Problem, sets this to the list
		print("CRAZY and amazing explosion happened in a distant universe. Lucky you weren't part of that.")
		return currentList
	else:
		## del currentList[donefor] <-- use for mega!!!
		for r in range(1,donefor):
			effected = currentList[r]
			newinfo = ""
			oldrocks = 0
			if effected[-2].isdigit(): ##checks if rocks are double digit number on planet
				for i in range(len(effected)-2): ##constructs a new string for planet info
					newinfo = newinfo + effected[i]
				oldrocks = int(effected[-1])+(10*int(effected[-2]))
			else:
				for i in range(len(effected)-1):
					newinfo = newinfo + effected[i]
				oldrocks = int(effected[-1])
			newinfo = newinfo+str(oldrocks+r*10)
			currentList[r] = newinfo
		print(currentList)
	del currentList[donefor]
	print("WOWZERS A CRAZY ROGUE AMAZING EXPLOSION HAPPENED IN PLANET ",donefor)
	print("That planet is done for, no more planet ", donefor)
	return currentList


def coolaliens(currentList,posi,level): ##when player confronts aliens
	global Afuel
	global Arocks
	#print (posi)
	effected = currentList[posi] ##effected planet is the position the player is on list

	if level > int(effected[0]): ## aliens are less smart
		#print("effected: ", effected[0])
		print("you are much smarter than the aliens")
		collectrocks(currentList,posi)

		if effected[3].isdigit(): ## checks if fuel number is double digit on planet because if its not a digit it would be dash in list
			planFuel = int(effected[3])+(10*int(effected[2]))
		else:
			planFuel = int(effected[2])
		takeaway = random.randint(1,planFuel)
		print("Fuel you recieve: ",takeaway)
		newplanFuel = str(planFuel - takeaway) ##make into string so we can attact it to planetinfo string
		planetinfo = ""
		accum = 0
		for n in range(2): ##reconstructs planet information string
			planetinfo = planetinfo+effected[n]
			accum = accum + 1
		planetinfo = planetinfo+newplanFuel
		if len(newplanFuel) == 2:
			accum = accum+2
		else:
			accum = accum+1
		for n in range(accum,len(effected)):
			planetinfo = planetinfo+effected[n]
		currentList[posi] = planetinfo #replace old information w/ new :D
		Afuel = Afuel + takeaway
		#print(currentList)
		print(Afuel)
		return(currentList)
			
	elif level == int(effected[0]): ## aliens are equal smart
		print("The aliens are just as smart as you...")
		collectrocks(currentList,posi)
		if effected[3].isdigit(): ## checks if fuel number is double digit on planet because if its not a digit it would be dash in list
			planFuel = int(effected[3])+(10*int(effected[2]))
		else:
			planFuel = int(effected[2])
		takeaway = random.randint(1, int(0.5*Afuel))
		print("Fuel taken from you: ",takeaway)
		Afuel = Afuel-takeaway
		print("Current fuel you have: ",Afuel)
		return (currentList)
		

	elif level < int(effected[0]): ##could have also used else. but this elif statement describes it better...
		print("The aliens are way smarter than you!")
		collectrocks(currentList,posi)
		if effected[3].isdigit(): ## checks if fuel number is double digit on planet because if its not a digit it would be dash in list
			planFuel = int(effected[3])+(10*int(effected[2]))
		else:
			planFuel = int(effected[2])
		takeaway = random.randint(1, Afuel)
		print("Fuel taken from you: ",takeaway)
		Afuel = Afuel-takeaway
		print("Current fuel you have: ",Afuel)
		return (currentList)
				

def collectrocks(currentList,posi): ##non fruitful function that appends collected rocks to global Arock variable
	global Arocks
	effected = currentList[posi]
	
	onethird = round((1/3),2) ##rounds one third to 2 decimal places
	efPlanet = currentList[posi]
	newinfo = ""
	oldrocks = 0
	if efPlanet[-2].isdigit():
		for i in range(len(efPlanet)-2):
			newinfo = newinfo + effected[i]
		oldrocks = int(efPlanet[-1])+(10*int(efPlanet[-2]))
	else:
		for i in range(len(efPlanet)-1):
			newinfo = newinfo + efPlanet[i]
		oldrocks = int(efPlanet[-1])
	newinfo = newinfo+str(oldrocks - int(onethird*oldrocks)) ##int rounds the rocks to an int
	currentList[posi] = newinfo
	Arocks.append(int(onethird*oldrocks))
	#print(currentList)
	print("current collected rocks: ",Arocks)
		
		
def roll_dice(lst, pos):
	#for dice roll
	#random.randomize()
	advance = random.randint(1,7)
	return (circularmovement(lst, pos, advance))


def circularmovement(lst, pos, advance):
	length = len(lst)
	counter = 0
	if pos > length -1:
		return -1
	while counter < advance:
		pos = pos + 1
		counter = counter + 1
		if pos > (length -1):
			pos = 0
	return pos


def finalresults(currentList, posi):
	global times_played ##for these globals, we aren't changing them ==> just showing them
	global moveFlag
	global civ_level
	global Afuel
	global alive
	global name
	global Arocks
	global play
	print("End of this game... results ----------")
	print("Game that took place:",times_played)
	if alive == False:
		print("Game ended because you died!")
	elif moves >= p_moves:
		print("Game ended because you played max amount of moves!")
	print("Showing final game board...")
	print(presentlist(currentList,posi))

	print("Astronaut "+ name + " has civilization level " + str(civ_level) + " He is in position " + str(posi) )
	print("You finished with ", Afuel," fuel")
	print("You finished with these cool rocks: ",Arocks)
	#play = input("Play again? (y/n)")

	
def FINALENDGAMEresults(currentList):
	global times_played
	global wins
	global total_rocks
	print("Total games played: ",times_played)
	print("Total games won: ",wins)
	rockBinary(currentList)


def rockBinary(currentList): ##takes list of planet info, extracts rock amounts and then converts them to binary code based off if even or odd amount
	planet_rock_list = []
	binary_list = []
	binary_number = 0
	print("To conclude, program will do a binary conversion!!")
	print("Taking rock specimens...")
	
	for y in range(len(currentList)):
		usedRocks = 0
		effected = currentList[y]
		if effected[-2].isdigit():
			usedRocks = (int(effected[-2])*10)+(int(effected[-1]))
		else:
			usedRocks = int(effected[-1])
		planet_rock_list.append(usedRocks)
	print("List of rocks in planets: ",planet_rock_list)
	for u in range(len(planet_rock_list)):
		if (planet_rock_list[u]%2) == 0:
			binary_list.append(0)
		else:
			binary_list.append(1)
	print("Binary conversion of list: ",binary_list)
	binary_list.reverse()
	for p in range(len(binary_list)):
		binary_number = binary_number+((2**p)*int(binary_list[p]))
	print("Binary number: ",binary_number)

	
##Top level ~~~ //^_^//

#To Do:
#bugs
#Rock/binary thing

import random   
##print(AMAZINGEXPLODEXD(presentlist(txttolist(),3),3)) ##3 is just arbetrary posisions
total_rocks = []
times_played = 0
wins = 0

play = input("Would you like to play (y/n) ?	")

while play == "y":
	moves = 0 ## resets all these variables to zero if player wants to play again
	moveFlag = False ## flag changes to true if max moves is hit
	Afuel = 10
	Arocks = []
	civ_level = 0
	alive = True
	p_pos = 0
	win_type = ""
	
	planet_lst = txttolist()
	length = len(planet_lst)
	print("Please enter the following information to set up game:")


	py_planet_cond = input("Do you want a planet python (y/n)? ")

	#ask user introduction questions, set initial values
	name = input("What is your name?: ")
	p_moves = int(input("How many moves do you want? (1-10): "))
	p_fuel = int(input("How many litres of fuel would you like to start with? (max 100): "))
	p_civ = int(input("What is you civilization level? (0-3): "))
	mild_explosion = input("Would you like mild explosions to occur? (y/n): ")
	amaz_explosion = input("Would you like amazing explosions to occur? (y/n) ")

	if py_planet_cond == "y":
		py_planet = int(input("What is the location of the Python Planet? (1-7): "))

	elif:
		py_planet = len(planet_lst) + 1 #player position will never be equal to the position of the non-existant Python Planet

	while p_pos != py_planet and moves < p_moves and alive == True:
		#Explosions
		if p_pos != 0:
			if mild_explosion == "y":
				planet_lst = mildexplode(planet_lst)
			if amaz_explosion == "y":
				planet_lst = AMAZINGEXPLODEXD(planet_lst, p_pos)
		
		#have player choose whether to choose planet location or roll dice
		move_choice = input("Do you want to roll the dice (r) or choose (c) a planet index (r/c) ?  ")

		if move_choice == "r":
			p_pos = roll_dice(planet_lst, p_pos)

		elif move_choice == "c":
			p_pos = int(input("Enter an integer from 0 to " +  str(length - 1)))

		planet_lst = presentlist(planet_lst, p_moves)

		#checks if astronaut is on PythonPlanet
		if p_pos != py_planet:
			planet_lst = coolaliens(planet_lst, p_pos, p_civ)
			if Afuel == 0:
				alive = False
				print("You are stranded because you have 0 fuel left. You are destined to die on Planet #", p_pos)
		elif p_pos == py_planet:
			win_type = "py_planet"
	
	finalresults(planet_lst, p_pos)

	#asks play question again at the end of the game
	play = input("Would you like to play again (y/n) ?	") #already in finalresults

if play == "y":
	FINALENDGAMEresults(planet_lst)
	print(coolaliens(presentlist(txttolist(),3), 3,1))
if play == "n":
	FINALENDGAMEresults(planet_lst)
	print("Goodbye!")

#order of functions that need to be called:
	#Check explosions
	#Aliens
	#Rocks
		#If player is not stranded, player collects 1/3 (integer) of rocks on planet, planet's rocks decrease
	#Fuel: if astronaut lost all fuel, he dies

#List of functions w/ arguments, not parameters:

#txttolist - translates planets.txt to a list

#presentlist(putinList, total_moves, moves) - prints planets.txt

#mildexplode(currentlist) -
	#only causes more rocks to become available if it occurs
	#returns planet_lst

#AMAZINGEXPLODEXD(currentlist, pos) -
	#Death Star's the planet, board shrinks, astronaut dies,
	#planet indexes shift
	#returns planet_lst

#coolaliens(currentList, pos, p_civ)
	#compares p_civ v. alien_civ
	#fuel levels - modifies Afuel, currentList fuel levels

#collectrocks(currentList, pos)
	#appends new rocks to global Arocks list

#circularmovement(currentLst, pos, roll)
	#moves player to next planet
	#returns new position

#finalresults(currentList, pos)
	#prints game results for the player to see

#rockbinary
	#for secret code at the end
	
