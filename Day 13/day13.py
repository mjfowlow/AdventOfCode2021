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


def problem2():
    #Read the input
    input = open("input.txt")
    data = input.read().split("\n\n")
    

    dots_coordinates = data[0].split("\n")
    folds = data[1].split("\n")

    #Get greatest x and y values
    greatest_x = 0
    greatest_y = 0

    for coordinates in dots_coordinates:
        x_value = int(coordinates.split(",")[0])
        y_value = int(coordinates.split(",")[1])

        if x_value > greatest_x:
            greatest_x = x_value
        if y_value > greatest_y:
            greatest_y = y_value


    #Create a empty matrix with y rows and x columns
    paper = [["."] * (greatest_x + 1) for i in range(greatest_y + 1)]

    #Iterate through coordinates adding dots at the coordinates
    for coordinates in dots_coordinates:
        x_coord = int(coordinates.split(",")[0])
        y_coord = int(coordinates.split(",")[1])

        paper[y_coord][x_coord] = '#'
    

    #Iterate throuhg the folds
    for fold in folds:
        fold = fold.split(" ")[2]
        fold_line = int(fold.split("=")[1])

        #If the fold line is 'y=..' it is a vertical fold up
        if fold[0] == 'y':
            #Create a new paper with new dimensions
            new_paper =  [["."] * (len(paper[0])) for i in range(fold_line)]
            
            for y in range(fold_line):
                for x in range(len(paper[0])):
                    #Get the upper and lower values
                    upper_value = paper[y][x]
                    lower_value = paper[-y-1][x]

                    #If either value is a dot set a dot at position[y][x] in the new paper
                    if upper_value == "#" or lower_value == "#":
                        new_paper[y][x] = "#"

        #If the fold line is "x=..." then have a horizontal fold to the left"
        if fold[0] == 'x':

            #Create new paper with new dimensions
            new_paper =  [["."] * (fold_line) for i in range(len(paper))]

            #iterate through each position on both sides of the fold line
            for x in range(fold_line):
                for y in range(len(paper)):
                    #get the values on the left and right side
                    left_value = paper[y][x]
                    right_value = paper[y][-x-1]

                    #If either value is a dot set a dot at position[y][x] in the new paper
                    if left_value == "#" or right_value == "#":
                        new_paper[y][x] = "#"
        
        paper = new_paper
    
    for row in paper:
        print("".join(row))

problem2()