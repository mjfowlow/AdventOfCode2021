#Day 9
print("--- Day 9: Smoke Basin ---")

#                                   --- Problem 1 ---
# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents
# release smoke into the caves that slowly settles like rain.
# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much 
# safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).
# Smoke flows to the lowest point of the area it's in.
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a 
# location can be.
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. 
# Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of 
# the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
# The risk level of a low point is 1 plus its height.
# Find all of the low points on your heightmap. 
# What is the sum of the risk levels of all low points on your heightmap?

def problem1(rows):
    #****** This problem is used by problem 2 so it is passed the data ******
    
    #Intialize the sum of risk levels to 0
    sum_risk_levels = 0

    #Create a list of the cordinates of the low points to be used in problem 2
    low_points = []

    #Iterate through each row and each value in a row
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            #Set low point to true
            low_point = True
            
            #Get height
            height = int(row[j])

            #Get the value above as along as it is not the first column.
            if i > 0:
                above_height = int(rows[i-1][j])
                #If the height above is less than or equal then the height set low_point to false
                if above_height <= height:
                    low_point = False
            
            #Get the below point as long as it isn't the last row and we haven't already proved it isn't a low point
            if i != len(rows) - 1 and low_point:
                below_height = int(rows[i+1][j])
                #If the height below is less than or equal then the height set low_point to false
                if below_height <= height:
                    low_point = False

            #Get the point to the left as long as it isnt the first value in a row and it is still considered a low point
            if j > 0 and low_point:
                left_height = int(rows[i][j-1])
                #If the height to the left is less than or equal then the height set low_point to false
                if left_height <= height:
                    low_point = False
            
            #Get point to the right aas long as it isn't the last value in a row and the point is still considered a low point
            if j != len(row) - 1 and low_point:
                right_height = int(rows[i][j+1])
                #If the height to the right is less than or equal then the height set low_point to false
                if right_height <= height:
                    low_point = False
            
            #If after comparing to all adjacent values the point is still a low point 
            #Calculate the risk level and adding it to the running sum 
            if low_point:
                risk_level = 1 + height
                sum_risk_levels += risk_level
                #Add coordinated to a list to be used in problem 2
                low_points.append((i,j))

    #Print the solution for problem 1 after checking every point
    print("Problem 1 Output:", sum_risk_levels)

    #Return the list of low point for problem 2
    return low_points


#                                       --- Problem 2 ---
# Next, you need to find the largest basins so you know what areas are most important to avoid.
# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin,
# although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations 
# will always be part of exactly one basin.
# The size of a basin is the number of locations within the basin, including the low point.
# What do you get if you multiply together the sizes of the three largest basins?

def problem2():
    #Read the input and split by rows
    input = open("input.txt")
    rows = input.read().split("\n")

    #Get list of low_points
    low_points = problem1(rows)

    #Basin sizes to keep trakc of the size of all the basins
    basin_sizes = []

    #Use breadth first search to get the number of elements in basins
    for low_point in low_points:
        #Create visited list and queue
        visited_list = []
        queue = []

        #Add low point to queue
        queue.append(low_point)
        #Mark low point as visited
        visited_list.append(low_point)

        #Iterate while queue is not empty
        while queue:
            #Get the next point
            point = queue.pop(0)

            #Get row and set coordinates
            row = rows[point[0]]
            i = point[0]
            j = point[1]

            #Get neighbors and add to a list if their heigh does not equal 9
            neighbors = []
            #Get the neighbor above as along as it is not the first column.
            if i > 0:
                above_neighbor = int(rows[i-1][j])
                if above_neighbor != 9:
                    neighbors.append((i-1, j))   
            
            #Get the below point as long as it isn't the last row
            if i != len(rows) - 1:
                below_neighbor = int(rows[i+1][j])
                if below_neighbor != 9:
                    neighbors.append((i+1,j))

            #Get the point to the left as long as it isnt the first value in a row
            if j > 0:
                left_neighbor = int(rows[i][j-1])
                if left_neighbor != 9:
                    neighbors.append((i,j-1))
                    
            #Get point to the right as long as it isn't the last value in a row 
                if j != len(row) - 1 and low_point:
                    right_neighbor = int(rows[i][j+1])
                    if right_neighbor != 9:
                        neighbors.append((i,j+1))        
            
            #Add each neighbor to the queue if it hasnt already been visited 
            for neighbor in neighbors:
                if not neighbor in visited_list:
                    queue.append(neighbor)
                    visited_list.append(neighbor)
        
        #Our basin size will the number of points we visited
        basin_sizes.append(len(visited_list))
            
    #Get the three largest basins and multiply them
    sorted_basin_sizes = sorted(basin_sizes, reverse=True)
    print("Problem 2 Output:", sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2])

problem2()