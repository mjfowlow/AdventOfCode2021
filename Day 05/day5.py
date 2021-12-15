#Day 5
print("--- Day 5: Hydrothermal Venture ---")

#                       --- Problem 1 ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly 
# produce large, opaque clouds, so it would be best to avoid them if possible.
# They tend to form in lines; the submarine helpfully produces a list of nearby lines of 
# vents (your puzzle input) for you to review.
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1
# are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. 
# These line segments include the points at both ends. In other words:
#       - An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#       - An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
# To avoid the most dangerous areas, you need to determine the number of points where at 
# least two lines overlap. 
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

def problem1():
    #Read input 
    input = open("input.txt")
    lines = input.read().split("\n")

    #Create a list holding 1000 lists that hold 1000 zeros
    hydrothermal_vents = []
    for i in range(1000):
        zeros_list = [0] * 1000
        hydrothermal_vents.append(zeros_list)

    #Iterate through each line (line looks like "x1,y1 - > x2,y2")
    for line in lines:
        #Seperate the coordinates (point looks like ["x1,y1", "x2,y2"])
        point = line.split(" -> ")
        #Get the exact coordinates
        x1 = int(point[0].split(",")[0])
        y1 = int(point[0].split(",")[1])
        x2 = int(point[1].split(",")[0])
        y2 = int(point[1].split(",")[1])

        #Have a vertical line
        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2+1):
                    hydrothermal_vents[x1][i] += 1
            else:
                for i in range(y2, y1+1):
                    hydrothermal_vents[x1][i] += 1
        #Have a horizontal line
        if y1 == y2:
            if x1 < x2:
                for i in range(x1, x2+1):
                    hydrothermal_vents[i][y1] += 1
            else:
                for i in range(x2, x1+1):
                    hydrothermal_vents[i][y1] += 1
    
    #Count the spots greater then 2
    sum = 0
    #iterate through each list and value
    for row in hydrothermal_vents:
        for value in row:
            #If greater than 1 incremnt sum
            if value > 1:
                sum += 1
    
    print("Problem 1 Output:", sum)

problem1()


#                           --- Problem 2 ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full 
# picture; you need to also consider diagonal lines.
# Because of the limits of the hydrothermal vent mapping system, the lines in your list will
# only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:
#       - An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
#       - An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# You still need to determine the number of points where at least two lines overlap.
# Consider all of the lines. At how many points do at least two lines overlap?

def problem2():
    #Read input 
    input = open("input.txt")
    lines = input.read().split("\n")

    #No value is greater then 1000 so reate a list holding 1000 lists that hold 1000 zeros
    hydrothermal_vents = []
    for i in range(1000):
        zeros_list = [0] * 1000
        hydrothermal_vents.append(zeros_list)

    #Iterate through each line (line looks like "x1,y1 - > x2,y2")
    for line in lines:
        #Seperate the coordinates (point looks like ["x1,y1", "x2,y2"])
        point = line.split(" -> ")
        #Get the exact coordinates
        x1 = int(point[0].split(",")[0])
        y1 = int(point[0].split(",")[1])
        x2 = int(point[1].split(",")[0])
        y2 = int(point[1].split(",")[1])

        #Have a vertical line 
        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2+1):
                    hydrothermal_vents[x1][i] += 1
            else:
                for i in range(y2, y1+1):
                    hydrothermal_vents[x1][i] += 1
        #Have a horizontal line
        elif y1 == y2:
            if x1 < x2:
                for i in range(x1, x2+1):
                    hydrothermal_vents[i][y1] += 1
            else:
                for i in range(x2, x1+1):
                    hydrothermal_vents[i][y1] += 1
        #Otherwise have diagonal line
        else:
            #If x1 < x2 then start with the first coordinates
            if x1 < x2:
                x_coordinate = x1
                y_coordinate = y1
                #If y1 < y2 then at each step we increment both x_coordinate and y_coordinate
                if y1 < y2:
                    while x_coordinate < x2 + 1:
                        hydrothermal_vents[x_coordinate][y_coordinate] += 1
                        x_coordinate += 1
                        y_coordinate += 1
                #If x1 < x2, y1 > y2 then we increment x coordinate and decremnt y coord at each step
                else:
                    while x_coordinate < x2 + 1:
                        hydrothermal_vents[x_coordinate][y_coordinate] += 1
                        x_coordinate += 1
                        y_coordinate -= 1
            #If x2 < x1 we start at the x2,y2 coordinate
            else:
                x_coordinate = x2
                y_coordinate = y2
                #If y2 < y1 we increment x coord and y coord at each step
                if y2 < y1:
                    while x_coordinate < x1 + 1:
                        hydrothermal_vents[x_coordinate][y_coordinate] += 1
                        x_coordinate += 1
                        y_coordinate += 1
                #If y2 < y1 we increment x coord and decremnt y coord at each step
                else:
                    while x_coordinate < x1 + 1:
                        hydrothermal_vents[x_coordinate][y_coordinate] += 1
                        x_coordinate += 1
                        y_coordinate -= 1 

    #Count the spots greater then 2
    sum = 0
    #iterate through each list and value
    for row in hydrothermal_vents:
        for value in row:
            #If greater than 1 incremnt sum
            if value > 1:
                sum += 1
    print("Problem 2 Output:", sum)

problem2()