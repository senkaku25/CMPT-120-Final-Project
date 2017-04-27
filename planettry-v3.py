####-----------------------FUNCTIONS-------------------------###
def txttolist():
	useFile = verification("Would you like to upload a custom map (write in file with .txt) or use the default? (d): ", "d", None, "string")

	if useFile == "d" :
		useFile = "planets.txt"

	fileRef = open(useFile,"r") # opening file to be read
	localList=[]

	for line in fileRef:
		string = line[0:len(line)-1]  # eliminates trailing '\n'
									# of each line
		localList.append(string)  # adds string to list

	fileRef.close()
	
	for x in range(len(localList)):
		localList[x] = localList[x].split("-")
	return(localList)
	##Use localList to access planets


def presentlist(putinList,moves,py_plan): ##presents list of planets to player so they can see map
        global py_planet_cond
        global py_planet
        print("Here is your map: ")
        print("Planet", "Civ-Level", "Fuel", "Rocks: ")

        newstr = ""
        #new version
        for x in range(len(putinList)):
                #putinList[x] = putinList[x].split("-")
                newstr = newstr + str(x) + "	 "

                for i in range(len(putinList[x])):
                        newstr = newstr + putinList[x][i] + "	 "

                if p_pos == x:
                        newstr = newstr + "	<--- Astronaut"
                if py_planet_cond == 'y':
                        if py_planet == x:
                                newstr = newstr + "	<=====PYTHON PLANET!!"

                print(newstr)
                newstr = ""
                print()

        return putinList


def mildexplode(currentList):
	lenny = len(currentList)*5
	donefor = random.randint(1,lenny)
	if donefor >= len(currentList):
		print("Mild explosion happened in a galaxy far, far away!!")
		return currentList
	else:
		## del currentList[donefor] <-- use for mega!!!
		for r in range(1,donefor):
			effected = currentList[r]
			newinfo = []
			oldrocks = int(effected[2])
			newrocks = r*10+oldrocks
			newinfo.extend([effected[0],effected[1],str(newrocks)])
			currentList[r] = newinfo

	print("A mild explosion happened in planet:",donefor, "!!")
	return currentList


def AMAZINGEXPLODEXD(currentList,posi):
	global py_planet
	lenny = len(currentList)*5
	donefor = random.randint(1,lenny)
	if posi == donefor:
		print("OH NO!! You got caught in a BIG AMAZING explosion!! You died because it was so big!")
		return -1 ##kills player
	if donefor >= len(currentList): #Problem, sets this to the list
		print("An amazing explosion happened in a distant universe. Lucky you weren't part of that.")
		return currentList
	else:
		## del currentList[donefor] <-- use for mega!!!
		for r in range(1,donefor):
			effected = currentList[r]
			newinfo = []
			oldrocks = int(effected[2])
			newrocks = r*10+oldrocks
			newinfo.extend([effected[0],effected[1],str(newrocks)])
			currentList[r] = newinfo
			py_planet = py_planet - 1

	del currentList[donefor]
	print("An amazing explosion just occured on planet #",donefor)
	print("That planet is done for, no more planet #", donefor)
	return currentList


def coolaliens(currentList,posi,level): ##when player confronts aliens
        global p_fuel
        global Arocks


        effected = currentList[posi]



        if level > int(effected[0]): ## aliens are less smart
                #print("effected: ", effected[0])
                print("You are much smarter than the aliens")
                collectrocks(currentList, posi)
                planFuel = int(effected[1])
                if planFuel > 0:
                        takeaway = random.randint(1, planFuel)
                else:
                        takeaway = 0
                print("Fuel you receive: ",takeaway)
                newplanFuel = str(planFuel - takeaway) ##make into string so we can attact it to planetinfo string
                planetinfo = []
                planetinfo.extend([effected[0],str(newplanFuel),effected[2]])

                currentList[posi] = planetinfo #replace old information w/ new :D
                p_fuel = p_fuel+takeaway
                print("Current fuel: ",p_fuel)
                return(currentList)

        elif level == int(effected[0]): ## aliens are equal smart
                print("The aliens are just as smart as you...")
                collectrocks(currentList,posi)

                planFuel = int(effected[1])
                takeaway = random.randint(1,(p_fuel//2))
                newplanFuel = str(planFuel - takeaway)
                planetinfo = []
                planetinfo.extend([effected[0],str(newplanFuel),effected[2]])
                currentList[posi] = planetinfo                        
                print("Fuel taken from you: ",takeaway)
                p_fuel = p_fuel-takeaway
                print("Current fuel you have: ",p_fuel)
                return (currentList)


        elif level < int(effected[0]): ##could have also used else. but this elif statement describes it better...
                print("The aliens are way smarter than you!")

                planFuel = int(effected[1]) 
                takeaway = random.randint(1, p_fuel)
                print("Fuel taken from you: ",takeaway)
                p_fuel = p_fuel-takeaway
                print("Current fuel you have: ",p_fuel)
                if p_fuel != 0:
                        collectrocks(currentList,posi)
                return (currentList)


def collectrocks(currentList,posi): ##non fruitful function that appends collected rocks to global Arock variable
	global Arocks
	efPlanet = currentList[posi]
	newinfo = []
	oldrocks = 0

	oldrocks = int(efPlanet[2])

	newinfo.extend([efPlanet[0],efPlanet[1],str(oldrocks - int(oldrocks//3))])
	currentList[posi] = newinfo
	Arocks.append(int(oldrocks//3))
	#print(currentList)
	print("Current collected rocks: ",Arocks)


def roll_dice(lst, pos):

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
	global p_civ
	global p_fuel
	global alive
	global name
	global Arocks
	global play
	global py_planet
	print("End of this game...")
	print("==============RESULTS=================")
	print("Games that took place:",times_played)
	if alive == False:
		print("Game ended because you died!")
	elif py_planet == p_pos:
		print("You reached the Python Planet and won!")
		p_fuel = 999
		Arocks.append(999)
	elif moves >= p_moves:
		print("Game ended because you played max amount of moves!")
	print("Showing final game board...")
	presentlist(currentList,posi,py_planet)

	print("Astronaut "+ name + ", has civilization level " + str(p_civ) + ", and is in position " + str(posi) )
	print("You finished with ", p_fuel," fuel")
	print("You finished with these cool rocks: ",Arocks)
	#play = input("Play again? (y/n)")


def FINALENDGAMEresults(currentList):
	global times_played
	global wins
	global total_rocks
	print("Total games played: ",times_played)
	print("Total games won: ",wins)
	print("Total rocks collected: ",total_rocks)
	rockBinary(currentList)


def rockBinary(currentList): ##takes list of planet info, extracts rock amounts and then converts them to binary code based off if even or odd amount
	planet_rock_list = []
	binary_list = []
	binary_number = 0
	print("To conclude, program will do a binary conversion!!")
	print("Taking rock specimens...")

	for y in range(len(currentList)):
		effected = currentList[y]
		usedRocks = effected[2]

		planet_rock_list.append(usedRocks)
	print("List of rocks in planets: ",planet_rock_list)
	for u in range(len(planet_rock_list)):
		if (int(planet_rock_list[u])%2) == 0:
			binary_list.append(0)
		else:
			binary_list.append(1)
	print("Binary conversion of list: ",binary_list)
	binary_list.reverse()
	for p in range(len(binary_list)):
		binary_number = binary_number+((2**p)*int(binary_list[p]))
	print("Binary number: ",binary_number)


def verification(prompt, cond1, cond2, vartype): #for user inputted values for variables, verifies the correct value
	bool = True

	if vartype == "integer":

		while bool == True:
			usr_in = input(prompt)

			if usr_in.isdigit() == False:
				print ("Whoops, try again")

			elif int(usr_in) < cond1 or int(usr_in) > cond2:
				print ("Whoops, try again")

			elif int(usr_in) >= cond1 and int(usr_in) <= cond2:
				bool = False
		return int(usr_in)

	elif vartype == "string":

		while bool == True:
			usr_in = input(prompt)

			if usr_in.isalpha() == False:
				print ("Whoops, try again")


			elif usr_in == cond1 or usr_in == cond2:
				bool = False

			elif usr_in != cond1 and usr_in != cond2:
				print("Whoops, try again")

		return str(usr_in)

##Top level ~~~ //^_^//

#To Do:
#bugs


import random
##print(AMAZINGEXPLODEXD(presentlist(txttolist(),3),3)) ##3 is just arbetrary posisions
total_rocks = []
times_played = 0
wins = 0

play = verification("Would you like to play? (y/n) ", "y", "n", "string")
if play == "n":
	no_play = True #for if/elif/elif at the end of top level

while play == "y":
        moves = 0 ## resets all these variables to zero if player wants to play again
        moveFlag = False ## flag changes to true if max moves is hit
        p_fuel = 0
        Arocks = []
        p_civ = 0
        alive = True
        p_pos = 0
        win_type = ""

        planet_lst = txttolist()
        length = len(planet_lst)
        print("Please enter the following information to set up game: ")

        py_planet_cond = verification("Do you want a planet python (y/n)? ", "y", "n", "string")


        name = input("What is your name?: ")
        p_moves = verification("How many moves do you want? (1-10): ", 1, 10, "integer")
        p_fuel = verification("How many litres of fuel would you like to start with? (max 100): ", 0, 100, "integer")
        p_civ = verification("What is you civilization level? (0-3): ", 0, 3, "integer")
        mild_explosion = verification("Would you like mild explosions to occur? (y/n): ", "y", "n", "string")
        amaz_explosion = verification("Would you like amazing explosions to occur? (y/n) ", "y", "n", "string")

        if py_planet_cond == "y":
                py_planet = verification("What is the location of the Python Planet? (1-7): ", 1, 7, "integer")

        elif py_planet_cond == "n":
                py_planet = len(planet_lst) + 1 #player position will never be equal to the position of the non-existant Python Planet

        while p_pos != py_planet and moves < p_moves and alive == True:
                #Explosions
                if p_pos != 0:
                        if mild_explosion == "y":
                                planet_lst = mildexplode(planet_lst)
                        if amaz_explosion == "y":
                                planet_lst = AMAZINGEXPLODEXD(planet_lst, p_pos)

                #have player choose whether to choose planet location or roll dice
                move_choice = verification("Do you want to roll the dice or choose a planet index? (r/c): ", "r", "c", "string")

                if move_choice == "r":
                        p_pos = roll_dice(planet_lst, p_pos)

                elif move_choice == "c":
                        p_pos_ver = "Enter an integer from 0 to " + str(length - 1) + ": "
                        p_pos = verification(p_pos_ver, 0, (length - 1), "integer")
                planet_lst = presentlist(planet_lst, p_moves,py_planet)
                if planet_lst == -1:
                        alive = False

                #checks if astronaut is on PythonPlanet
                if p_pos != py_planet:
                        planet_lst = coolaliens(planet_lst, p_pos, p_civ)
                        if p_fuel <= 0:
                                alive = False
                                print("You are stranded because you have 0 fuel left. You are destined to die on Planet #", p_pos)
                elif p_pos == py_planet:
                        win_type = "py_planet"
                        wins = wins+1
                moves = moves +1
        total_rocks.append(Arocks) ##accumulating all the rocks collected 
        times_played = times_played + 1 ##you played this many times!!
        finalresults(planet_lst, p_pos)

        #asks play question again at the end of the game
        play = verification("Would you like to play again? (y/n): ", "y", "n", "string") #already in finalresults
        if play == 'n':
                no_play = False

if play == "y":
        FINALENDGAMEresults(planet_lst)
        
elif play == "n" and no_play == False:
        FINALENDGAMEresults(planet_lst)
        print("Goodbye!")
        
elif play == "n" and no_play == True:
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
        #fuel levels - modifies p_fuel, currentList fuel levels

#collectrocks(currentList, pos)
        #appends new rocks to global Arocks list

#circularmovement(currentLst, pos, roll)
        #moves player to next planet
        #returns new position

#finalresults(currentList, pos)
        #prints game results for the player to see

#rockbinary
        #for secret code at the end

