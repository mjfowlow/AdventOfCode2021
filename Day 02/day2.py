#Day 2
print("--- Day 2: Dive! ---")

#                           --- Problem 1 ---
# Now, you need to figure out how to pilot this thing.
# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:
#    - forward X increases the horizontal position by X units.
#    - down X increases the depth by X units.
#    - up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, and so they have the 
# opposite result of what you might expect.
# The submarine seems to already have a planned course (your puzzle input). You should probably 
# figure out where it's going.
# Your horizontal position and depth both start at 0.
# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

def problem1():
    #Read input data
    input = open("input.txt")
    commands = input.read().split("\n")

    #Intizlize horizontal position and depth
    horizontal_position = 0
    depth = 0

    #Iterate through all commands
    for command in commands:
        #Split command up by direction and distance
        directions = command.split(" ")
        direction = directions[0]
        distance = int(directions[1])

        #Depending on direction update horizontal_position or depth
        if direction == "forward":
            horizontal_position += distance
        elif direction == "down":
            depth += distance
        else:
            depth -= distance
    
    #Print out the horizontal position times depth
    print("Problem 1 Output:", horizontal_position * depth)

problem1()

#                               --- Problem 2 ---
# Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine 
# manual and discover that the process is actually slightly more complicated.
# In addition to horizontal position and depth, you'll also need to track a third value, aim, which also
# starts at 0. The commands also mean something entirely different than you first thought:
#       - down X increases your aim by X units.
#       - up X decreases your aim by X units.
#       - forward X does two things:
#           - It increases your horizontal position by X units.
#           - It increases your depth by your aim multiplied by X.
# Using this new interpretation of the commands, calculate the horizontal position and depth you 
# would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?

def problem2():
    #Read input data
    input = open("input.txt")
    commands = input.read().split("\n")

    #Intizlize horizontal position, depth, and aim
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        #Split command up by direction and distance
        directions = command.split(" ")
        direction = directions[0]
        distance = int(directions[1])

        # If direction equals "forward" increase horizontal positon by distance and increase depth by aim x distance
        # If direction equals "down" or "up" increase or decrease aim accordingly
        if direction == "forward":
            horizontal_position += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        else:
            aim -= distance
        
    #Print horizontal position times depth to get your answer
    print("Problem 2 Output:", horizontal_position * depth)

problem2()