import random
def txttolist():
    useFile = input("Would you like to upload map(write in file with .txt) or use defalt(d)? ")
    if useFile == "d":
        useFile = "planets.txt"
    fileRef = open(useFile,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list

    fileRef.close()
    print(localList)
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
            y = y+gr8+spaces+x+"   <=== Astronaught :)"+"\n"
        else:
            y =y+gr8+spaces+x+"\n"
    print(y)
    print(newPlist)
    return newPlist


def mildexplode(currentList):
    lenny = len(currentList)*5
    donefor = random.randint(1,lenny)
    if donefor >= len(currentList):
        return "Mild explosion happened in a galaxy far away!!"
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
        print(currentList)
    print("Wowzer, a mild explosion happened in planet:",donefor)
    return currentList

def AMAZINGEXPLODEXD(currentList,posi):
    import random
    lenny = len(currentList)*5
    donefor = random.randint(1,lenny)
    if posi == donefor:
        print("OH NO!! You got caught in a BIG AMAZING explosion!!! you died because it was so big!")
        return -1 ##kills player
    if donefor >= len(currentList):
        return "CRAZY and amazing explosion happened in a distant universe. Lucky you weren't part of that."
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
    print("WOWZERS A CRAZY ROGUE AMAZING EXPLOSION HAPPENED IN PLANNET ",donefor)
    print("That planet is done for, no more planet ", donefor)
    return currentList

def coolaliens(currentList,posi,level): ##when player confronts aliens
    global Afuel
    global Arocks
    effected = currentList[posi] ##effected planet is the position the player is on list

    if level > int(effected[0]): ## aliens are less smart
        print("you are much smarter than the aliens")
        collectrocks(currentList,posi)

        if effected[3].isdigit(): ## checks if fuel number is double digit on planet because if its not a digit it would be dash in list
            planFuel = int(effected[3])+(10*int(effected[2]))
        else:
            planFuel = int(effected[2])
        takeaway = random.randint(1,planFuel)
        print("Fuel you recieve: ",takeaway)
        newplanFuel = str(planFuel - takeaway) ##make into string so we can attact it planinfo string
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
        print(currentList)
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
    print(currentList)
    print("current collected rocks: ",Arocks)
        
        



def advance_circularly_list(lst,pos,advance):
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


def finalresults(currentList,posi):
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
    elif moveFlag == True:
        print("Game ended because you played max amount of moves!")
    print("Showing final game board...")
    print(presentlist(currentList,posi))

    print("Astronaut "+name+" has civilization level "+str(civ_level)" He is in position "+str(posi))
    print("You finished with ",Afuel," fuel")
    print("You finished with these cool rocks: ",Arocks)
    play = input("Play again? (y/n)")

    
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


import random   
##print(AMAZINGEXPLODEXD(presentlist(txttolist(),3),3)) ##3 is just arbetrary posisions
total_rocks = []
times_played = 0
wins = 0

while play == "y":
    moves = 0 ## resets all these variables to zero if player wants to play again
    moveFlag == False ## flag changes to true if max moves is hit
    Afuel = 10
    Arocks = []
    civ_level = 0
    alive = True
    posi = 0
    print("please enter information to set up game:")
    total_moves = int(input("How many moves do you want (1-10)?")
    py_planet_cond = input("Do you want a planet python (y/n)? ")
    if py_planet_cond == "y":
        py_planet = int(input("What is location of Python Planet (1-7)?"))
    else:
        py_planet = 10
    while pose != py_planet and moves < total_moves and alive == True:
        m_explossion = input("Would you like mild explosions (y/n)?")
        name = input("What is your name?")
        Afuel = int(input("How much fuel would you like? (10-50)"))
                      


print(coolaliens(presentlist(txttolist(),3), 3,1))
