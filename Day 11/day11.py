#Day 11
print("--- Day 11: Dumbo Octopus ---")

#                                               --- Problem 1 ---
# You enter a large cavern full of rare bioluminescent dumbo octopuses! They seem to not like the Christmas lights 
# on your submarine, so you turn them off for now.
# There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes 
# brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the 
# cave without disturbing the octopuses if you could predict when the flashes of light will happen.
# Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle input).
# The energy level of each octopus is a value between 0 and 9.
# You can model the energy levels and flashes of light in steps. During a single step, the following occurs:
#       - First, the energy level of each octopus increases by 1.
#       - Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses 
#         by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, 
#         it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. 
#         (An octopus can only flash at most once per step.)
#       - Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
# Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.
# Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. 
# How many total flashes are there after 100 steps?

def problem1():
    #Read the input
    input = open("input.txt")
    rows = input.read().split("\n")

    #Split each row into a list of numbers
    for i in range(len(rows)):
        line = rows[i]
        rows[i] = list(line)

    #Create a list of adjacent octopuses and intialize flashes
    adjacent_octopuses = []
    flashes = 0

    #Intialize step to 0
    step = 0

    #Complete 100 steps
    while step < 100:
        #Create an empty list to hold the coordinates of flashes so we don't increment them after being flashed
        flashed_list = [] 
        
        #Iterate through all the octopusues
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                energy_level = int(row[j])

                #if energy level is equal to 9 set it to 0, add to flashed list and add all adjacent octopuses to adjacent list
                if energy_level == 9:
                    rows[i][j] = 0 
                    flashes += 1
                    flashed_list.append((i,j))

                    #Add all surrounding values to a list
                    #If not first row add values above
                    if i > 0:
                        adjacent_octopuses.append((i-1,j))
                        if j > 0:
                            adjacent_octopuses.append((i-1,j-1))
                        if j < (len(row) - 1):
                            adjacent_octopuses.append((i-1, j+1))

                    #if not last row add values below
                    if i < (len(rows) - 1):
                        adjacent_octopuses.append((i+1,j))
                        if j > 0:
                            adjacent_octopuses.append((i+1,j-1)) 
                        if j < (len(row) - 1):
                            adjacent_octopuses.append((i+1, j+1))
                    
                    #if not first or last column add values to the left and right
                    if j > 0:
                        adjacent_octopuses.append((i, j-1))
                    if j < (len(row) - 1):
                        adjacent_octopuses.append((i, j+1))

                #If it does not equal 9 increment it
                else:
                    rows[i][j] = energy_level + 1

        #Not deal with all those adjacent octopusues
        while len(adjacent_octopuses) > 0:
            #Get and remove the octopus
            octopus_position = adjacent_octopuses.pop(len(adjacent_octopuses)-1)

            #If it has already been flashed continue
            if(octopus_position in flashed_list):
                continue

            #Get cordinates
            row = octopus_position[0]
            col = octopus_position[1]


            #If energy level is equal to 9 set it to 0, add to flashed list and add all adjacent octopuses to adjacent list
            if rows[row][col] == 9:
                rows[row][col] = 0 
                flashes += 1
                flashed_list.append((row,col))

                #Add all surrounding values to a list
                #If not first row add values above
                if row > 0:
                    adjacent_octopuses.append((row-1,col))
                    if col > 0:
                        adjacent_octopuses.append((row-1,col-1))
                    if col < (len(rows[0]) - 1):
                        adjacent_octopuses.append((row-1, col+1))

                #if not last row add values below
                if row < (len(rows) - 1):
                    adjacent_octopuses.append((row+1,col))
                    if col > 0:
                        adjacent_octopuses.append((row+1,col-1)) 
                    if col < (len(rows[0]) - 1):
                        adjacent_octopuses.append((row+1, col+1))
                
                #if not first or last column add values to the left and right
                if col > 0:
                    adjacent_octopuses.append((row, col-1))
                if col < (len(rows[0]) - 1):
                    adjacent_octopuses.append((row, col+1))    

            #If it does not equal 9 increment it
            else:
                rows[row][col] = int(rows[row][col]) + 1
        
        #Increment step
        step += 1

    print("Problem 1 Output:", flashes)

problem1()


#                                           --- Problem 2 ---
# It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: 
# the flashes seem to be synchronizing!
# If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to 
# navigate through the cavern. What is the first step during which all octopuses flash?

def problem2():
    #Read the input
    input = open("input.txt")
    rows = input.read().split("\n")

    #Split each row into a list of numbers
    for i in range(len(rows)):
        line = rows[i]
        rows[i] = list(line)

    #Calculate the number of octupuses
    num_octupuses = len(rows) * len(rows[0])

    #Create a list of adjacent octopuses and intialize flashes
    adjacent_octopuses = []

    #Intialize step to 1
    step = 1

    #Set all_flashed to False
    all_flashed = False

    #Complete 100 steps
    while not all_flashed:
        #Create an empty list to hold the coordinates of flashes so we don't increment them after being flashed
        flashed_list = [] 
        
        #Iterate through all the octopusues
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                energy_level = int(row[j])

                #if energy level is equal to 9 set it to 0, add to flashed list and add all adjacent octopuses to adjacent list
                if energy_level == 9:
                    rows[i][j] = 0
                    flashed_list.append((i,j))

                    #Add all surrounding values to a list
                    #If not first row add values above
                    if i > 0:
                        adjacent_octopuses.append((i-1,j))
                        if j > 0:
                            adjacent_octopuses.append((i-1,j-1))
                        if j < (len(row) - 1):
                            adjacent_octopuses.append((i-1, j+1))

                    #if not last row add values below
                    if i < (len(rows) - 1):
                        adjacent_octopuses.append((i+1,j))
                        if j > 0:
                            adjacent_octopuses.append((i+1,j-1)) 
                        if j < (len(row) - 1):
                            adjacent_octopuses.append((i+1, j+1))
                    
                    #if not first or last column add values to the left and right
                    if j > 0:
                        adjacent_octopuses.append((i, j-1))
                    if j < (len(row) - 1):
                        adjacent_octopuses.append((i, j+1))

                #If it does not equal 9 increment it
                else:
                    rows[i][j] = energy_level + 1

        #Not deal with all those adjacent octopusues
        while len(adjacent_octopuses) > 0:
            #Get and remove the octopus
            octopus_position = adjacent_octopuses.pop(len(adjacent_octopuses)-1)

            #If it has already been flashed continue
            if(octopus_position in flashed_list):
                continue

            #Get cordinates
            row = octopus_position[0]
            col = octopus_position[1]

            #If energy level is equal to 9 set it to 0, add to flashed list and add all adjacent octopuses to adjacent list
            if rows[row][col] == 9:
                rows[row][col] = 0
                flashed_list.append((row,col))

                #Add all surrounding values to a list
                #If not first row add values above
                if row > 0:
                    adjacent_octopuses.append((row-1,col))
                    if col > 0:
                        adjacent_octopuses.append((row-1,col-1))
                    if col < (len(rows[0]) - 1):
                        adjacent_octopuses.append((row-1, col+1))

                #if not last row add values below
                if row < (len(rows) - 1):
                    adjacent_octopuses.append((row+1,col))
                    if col > 0:
                        adjacent_octopuses.append((row+1,col-1)) 
                    if col < (len(rows[0]) - 1):
                        adjacent_octopuses.append((row+1, col+1))
                
                #if not first or last column add values to the left and right
                if col > 0:
                    adjacent_octopuses.append((row, col-1))
                if col < (len(rows[0]) - 1):
                    adjacent_octopuses.append((row, col+1))    

            #If it does not equal 9 increment it
            else:
                rows[row][col] = int(rows[row][col]) + 1

        #If length of flashed list is equal to the toal number of octupuses then all flashed
        if len(flashed_list) == num_octupuses:
            all_flashed = True
            print("Problem 2 Output:", step)
        
        #Increment step
        step += 1

problem2()