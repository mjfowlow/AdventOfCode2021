#Day 1
print("--- Day 1: Sonar Sweep ---")

#                                   --- Problem 1 ----
# As the submarine drops below the surface of the ocean, it automatically performs a sonar 
# sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input)
# appears: each line is a measurement of the sea floor depth as the sweep looks further and 
# further away from the submarine.
# The first order of business is to figure out how quickly the depth increases, just so you 
# know what you're dealing with - you never know if the keys will get carried into deeper 
# water by an ocean current or a fish or something.
# To do this, count the number of times a depth measurement increases from the previous measurement. 
# (There is no measurement before the first measurement.)
# How many measurements are larger than the previous measurement?

def problem1():
    #Read input data
    input = open("input.txt")
    lines = input.read().split("\n")

    #Get the first value
    previous_measurement = int(lines[0])
    #Number of increases
    increase_counter = 0

    #Iterate through all numbers starting at the second number
    for i in range(1,len(lines)):
        #Get next measurment
        next_measurement = int(lines[i])
        #If next measurement is greater then the previous incrment the counter
        if(next_measurement > previous_measurement):
            increase_counter += 1
        
        #Update the previous measurement
        previous_measurement = next_measurement

    print("Problem 1 Output:", increase_counter)

problem1()

#                                       --- Problem 2 ---
# Considering every single measurement isn't as useful as you expected: there's just too much 
# noise in the data.
# Instead, consider sums of a three-measurement sliding window.
# Your goal now is to count the number of times the sum of measurements in this sliding window 
# increases from the previous sum. So, compare A with B, then compare B with C, then C with D, 
# and so on. Stop when there aren't enough measurements left to create a new three-measurement sum
# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

def problem2():
    #Read input data
    input = open("input.txt")
    lines = input.read().split("\n")

    #Intialize previous window sum variable
    previous_window = int(lines[0]) + int(lines[1]) + int(lines[2])
    
    #Number of increases
    increase_counter = 0

    #Iterate through the list starting at the seocnd number
    for i in range(1, len(lines)-2):
        #Calculate the next window
        first_num = int(lines[i])
        second_num = int(lines[i + 1])
        third_num = int(lines[i + 2])
        next_window = first_num + second_num + third_num
        #If next window is greater previous window increase the counter
        if(next_window > previous_window):
            increase_counter += 1
        #Update previous window
        previous_window = next_window
    
    print("Problem 2 Output:", increase_counter)

problem2()


