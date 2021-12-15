#Day 7
print("--- Day 7: The Treachery of Whales ---")

#                                   --- Problem 1 ---
# A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!
# Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! 
# They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just 
# beyond where they're aiming!
# The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your 
# submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?
# There's one major catch - crab submarines can only move horizontally.
# You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you 
# need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible
# Each change of 1 step in horizontal position of a single crab costs 1 fuel.
# Determine the horizontal position that the crabs can align to using the least fuel possible. 
# How much fuel must they spend to align to that position?


def problem1():
    #Read the input data
    input = open("input.txt")
    positions = input.read().split(",")

    # convert the list of positons from strings to intgers
    positions= list(map(int, positions))

    #Get the largest integer in the list
    largest_value = max(positions)

    # We will keep track of the number of crabs at a certain position using a list
    # So number_at_positions[10] would represent the number of crabs at positon 10
    number_at_positions = []
    # Iterate through values from 0 to largest value found
    for i in range(largest_value + 1):
        # Add the number of times i appears in positions
        number_at_positions.append(positions.count(i))
    
    # Much like we did for keep track of the number of crabs at a position we will use a 
    # list to track how much fuel will be used to align at a position
    # So fuel_usage[10] would return the amount of fuel it would take to align all the crabs at position 10
    fuel_usage = []
    #Iterate through all the positions
    for i in range(len(number_at_positions)):
        #Reset fuel usage and set the position variable to i
        total_fuel_usage = 0
        position = i
        #Now iterate through all the positions calculating the fuel usage
        for j in range(len(number_at_positions)):
            #calculate the cost of going from position j to position and then multiply by the number of crabs at position j
            total_fuel_usage += abs(j-position) * number_at_positions[j]
        
        #Add the calculated fuel usage to the list
        fuel_usage.append(total_fuel_usage)

    #Print the minimum fuel ussage possible 
    print("Problem 1 Output:", min(fuel_usage))

problem1()

#                                       --- Problem 2 ---
# The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?
# As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal
# position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.
# As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on.
# Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! 
# How much fuel must they spend to align to that position?
# ***** Solution is almost the exact same as solution 1. Just change the formual for calulating cost ****

def problem2():
    #Read the input
    input = open("input.txt")
    positions = input.read().split(",")

    # convert the list of positons from strings to intgers
    positions= list(map(int, positions))

    #Get the largest integer in the list
    largest_value = max(positions)

    # We will keep track of the number of crabs at a certain position using a list
    # So number_at_positions[10] would represent the number of crabs at positon 10
    number_at_positions = []
    # Iterate through values from 0 to largest value found
    for i in range(largest_value + 1):
        # Add the number of times i appears in positions
        number_at_positions.append(positions.count(i))
    
    # Much like we did for keep track of the number of crabs at a position we will use a 
    # list to track how much fuel will be used to align at a position
    # So fuel_usage[10] would return the amount of fuel it would take to align all the crabs at position 10
    fuel_usage = []
    #Iterate through all the positions
    for i in range(len(number_at_positions)):
        #Reset fuel usage and set the position variable to i
        total_fuel_usage = 0
        position = i
        #Now iterate through all the positions calculating the fuel usage
        for j in range(len(number_at_positions)):
            #calculate the cost of going from position j to position 
            #Then use the formula (n(n+1)/2) to calculate the actual fuel cost [n(n+1)/2 represents n + n-1 + n-2  + ...  + n-(n-1)] 
            #and then multiply by the number of crabs at position j
            difference = abs(j-position)
            fuel_cost = (difference * (difference+1))/2
            total_fuel_usage += fuel_cost * number_at_positions[j]
        
        #Add the calculated fuel usage to the list
        fuel_usage.append(total_fuel_usage)

    #Print the minimum fuel ussage possible 
    print("Problem 2 Output:", int(min(fuel_usage)))

problem2()