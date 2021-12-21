#Day 13
print("--- Day 13: Transparent Origami ---")

#                                                   --- Problem 1 ---
# You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal
# imaging so you could tell ahead of time which caves are too hot to safely enter.
# Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:
#       Congratulations on your purchase! To activate this infrared thermal imaging camera system, please enter the code found on page 1 of the manual.
# Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to 
# open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots 
# and includes instructions on how to fold it up (your puzzle input).
# The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, 
# x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and
# the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper
# and "." is an empty, unmarked position
# Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold
# the paper up (for horizontal y=... lines) or left (for vertical x=... lines).
# Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line.
# Some dots can end up overlapping; in this case, the dots merge together and become a single dot.
# The transparent paper is pretty big, so for now, focus on just completing the first fold.
# dots that end up overlapping after the fold is completed count as a single dot.
# How many dots are visible after completing just the first fold instruction on your transparent paper?

def problem1():
    #Read the input
    input = open("input.txt")
    data = input.read().split("\n\n")
    

    dots_coordinates = data[0].split("\n")
    folds = data[1].split("\n")

    #Get greatest x and y values
    greatest_x = 0
    greatest_y = 0

    for coordinates in dots_coordinates:
        x = int(coordinates.split(",")[0])
        y = int(coordinates.split(",")[1])

        if x > greatest_x:
            greatest_x = x
        if y > greatest_y:
            greatest_y = y


    #Create a empty matrix with y rows and x columns
    paper = [["."] * (greatest_x + 1) for i in range(greatest_y + 1)]

    #Iterate through coordinates adding dots at the coordinates
    for coordinates in dots_coordinates:
        x = int(coordinates.split(",")[0])
        y = int(coordinates.split(",")[1])

        paper[y][x] = '#'

    #Get first fold and fold line
    first_fold = folds[0]
    first_fold = first_fold.split(" ")[2]
    fold_line = int(first_fold.split("=")[1])

    #If the fold line is 'y=..' it is a vertical fold up
    if first_fold[0] == 'y':
        
        #Create a new paper with new dimensions 
        new_paper =  [["."] * (len(paper[0])) for i in range(int(len(paper)/2))]
        
        #Intialize number dots to 0
        number_dots = 0

        for y in range(fold_line):
            for x in range(len(paper[0])):
                #Get the upper and lower values
                upper_value = paper[y][x]
                lower_value = paper[-y-1][x]

                #If either value is a dot set a dot at position[y][x] in the new paper
                if upper_value == "#" or lower_value == "#":
                    number_dots += 1
                    new_paper[y][x] = "#"
    
    #If the fold line is "x=..." then have a horizontal fold to the left"
    if first_fold[0] == 'x':

        #Create new paper with new dimensions
        new_paper =  [["."] * (int(len(paper[0])/2)) for i in range(len(paper))]

        #Intialize the number of dots to zero
        number_dots = 0

        #iterate through each position on both sides of the fold line
        for x in range(fold_line ):
            for y in range(len(paper)):
                #get the values on the left and right side
                left_value = paper[y][x]
                right_value = paper[y][-x-1]

                #If either value is a dot set a dot at position[y][x] in the new paper
                if left_value == "#" or right_value == "#":
                    number_dots += 1
                    new_paper[y][x] = "#"


    print("Problem 1 Output:", number_dots)

problem1()

#                                           --- Problem 2 ---
# Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.
# What code do you use to activate the infrared thermal imaging camera system?

def problem2():
    #Read the input
    input = open("input.txt")
    data = input.read().split("\n\n")
    
    #Get coordinates and folds in a list in a list
    coordinates = data[0].split("\n")
    folds = data[1].split("\n")

    #Create a set to hold the data coordinates, where each coordinate is a tuple ( (x,y) )
    dots_coordinates = set()
    for coordinate in coordinates:
        dots_coordinates.add(tuple([int(i) for i in coordinate.split(",")]))

    #Iterate through folds
    for fold in folds:
        #Get the type of fold ("x" or "y") and fold line value
        fold = fold.split(" ")[2]
        fold_line = int(fold.split("=")[1])

        #Create a new set of dots
        new_dots = set()
        
        #If fold equals "y" it is a vertical fold up
        if fold[0] == 'y':
            #Iterate through each coordinate 
            for coordinate in dots_coordinates:
                #If the y coordinates is greater then the fold line, we need to calculate the new y coordinate after folding
                if coordinate[1] > fold_line:
                    #To get the new y coordinate we do the calculation (2 x fold line - y-coordinate)
                    new_coordinate = (coordinate[0], fold_line * 2 - coordinate[1])
                    new_dots.add(new_coordinate)
                #If the y-coordinate is lesss then the fold line just add it to the new set of dots
                else:
                    new_dots.add(coordinate)
                
        #If the fold equals "x" it is a horizontal fold to the left
        if fold[0] == 'x':
            #Iterate trhoguh each coordinate
            for coordinate in dots_coordinates:
                #If the x-coordinate is less then the fold_line caluclate the new x-coord after folding 
                if coordinate[0] > fold_line:
                    new_coordinate = (fold_line * 2 - coordinate[0], coordinate[1])
                    new_dots.add(new_coordinate)
                #Otherwise add the coordinate to the new set fo coordinates
                else:
                    new_dots.add(coordinate)

        #Set the old coordinates as the new set of coordinates
        dots_coordinates = new_dots
    
    #Print the message
    print("\nProblem 2 Output:")
    for y in range(6):
        for x in range(50):
            if (x, y) in dots_coordinates:
                print("##", end="")
            else:
                print("..", end="")
        print()
    
problem2()