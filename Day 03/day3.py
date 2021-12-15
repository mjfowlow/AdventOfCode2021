#day 3
print("--- Day 3: Binary Diagnostic ---")

#                               --- Problem 1 ---
# The submarine has been making some odd creaking noises, so you ask it to produce a 
# diagnostic report just in case.
# The diagnostic report (your puzzle input) consists of a list of binary numbers which, 
# when decoded properly, can tell you many useful things about the conditions of the 
# submarine. The first parameter to check is the power consumption.
# You need to use the binary numbers in the diagnostic report to generate two new binary 
# numbers (called the gamma rate and the epsilon rate). The power consumption can then be
# found by multiplying the gamma rate by the epsilon rate.
# Each bit in the gamma rate can be determined by finding the most common bit in the 
# corresponding position of all numbers in the diagnostic report.
# The epsilon rate is calculated in a similar way; rather than use the most common bit, the 
# least common bit from each position is used.
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon 
# rate, then multiply them together. What is the power consumption of the submarine? (Be sure 
# to represent your answer in decimal, not binary.)

import copy
def problem1():
    #Read the input
    input = open("input.txt")
    numbers = input.read().split("\n")
	
    #Create a counter of zeros. One for every positon in the binary number
    common_bit = [0] * len(numbers[0])
    
    #Iterate through the numbers
    for number in numbers:
        #Iterate through each bit
        for i in range(len(number)):
            #Get bit
            bit = int(number[i])
            #If bit equals one incrment the value at bit position i in the list
            if bit == 1:
                common_bit[i] += 1
            #Otherwise decrement at bit position i
            else:
                common_bit[i] -= 1
    
    #Intialize the rates as empty strings. Will build the binary bit by bit
    gamma_rate = ""
    epsilon_rate = ""
    #Iterate through the common bit list
    for value in common_bit:
        #If value at position is less then 0 then 0 was the most common number
        if value > 0:
            #Therfore add a 1 to the gamma rate and a 0 to epsilon rate
            gamma_rate += "1"
            epsilon_rate += "0"
        #If value at position is greater then a 0 was the most common number
        else:
            #Therfore add a 0 to the gamma rate and a 1 to epsilon rate
            gamma_rate += "0"
            epsilon_rate += "1"
    
    #Convert rates to integers
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    
    #Mutiply the rates for the solution
    print("Problem 1 Output", gamma_rate * epsilon_rate)
	
problem1()

#                           --- Problem 2 ---
# Next, you should verify the life support rating, which can be determined by multiplying 
# the oxygen generator rating by the CO2 scrubber rating.
# Both the oxygen generator rating and the CO2 scrubber rating are values that can be found 
# in your diagnostic report - finding them is the tricky part. Both values are located using 
# a similar process that involves filtering out values until only one remains. Before 
# searching for either rating value, start with the full list of binary numbers 
# from your diagnostic report and consider just the first bit of those numbers. Then:
#       - Keep only numbers selected by the bit criteria for the type of rating value for which
#         you are searching. Discard numbers which do not match the bit criteria.
#       - If you only have one number left, stop; this is the rating value for which you are searching.
#       - Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
#       - To find oxygen generator rating, determine the most common value (0 or 1) in the current 
#         bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally 
#         common, keep values with a 1 in the position being considered.
#       - To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit 
#         position, and keep only numbers with that bit in that position. If 0 and 1 are equally 
#         common, keep values with a 0 in the position being considered.
# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 
# scrubber rating, then multiply them together. What is the life support rating of the submarine? 
# (Be sure to represent your answer in decimal, not binary.)

# Recursice method used to solve problem 2 
def get_rating(list, bit_position, rating_type):
    
    #If list only has one value left we have got our rating so return it
    if len(list) == 1:
        return list[0]
    
    else:
        # Make a string of all the bits at bit_position in each number
        bits = ''.join(line[bit_position] for line in list if line)
        # Count the number of 1 and 0 bits in the string
        number_1_bits = bits.count("1")
        number_0_bits = bits.count("0")
        # Depending on the rating we are trying to calculate set the common_bit to look for 
        if rating_type == "oxygen":
            if number_1_bits == number_0_bits or number_1_bits > number_0_bits:
                common_bit = "1"
            else:
                common_bit = "0"
        else:
            if number_1_bits == number_0_bits or number_1_bits > number_0_bits:
                common_bit = "0"
            else:
                common_bit = "1"
            
        # Remove numbers that do not share the common bit in bit_position
        i = 0
        while i < len(list):
            #Get number from the list
            number = list[i]
            #if it does not have the same value as the common_bit remove it
            if number[bit_position] != common_bit:
                list.pop(i)
                #Do not increment i since we removed an element
                continue
            #Id didnt remove a number increment i
            i += 1
        
        #Increment bit_position and call get_rating again
        return get_rating(list, bit_position+1, rating_type)
                

def problem2():
    #Get input data
    input = open("input.txt")
    lines = input.read().split("\n")
    
    #Make copy of the numbers so we do not ruin the orginial list
    number_list = copy.deepcopy(lines)
    #Send list of numbers and starting position to get_oxygen_generator_rating
    oxygen_generator_rating = get_rating(number_list, 0, "oxygen")
    
    #Make another copy to not modify the orginial list and call get rating
    number_list = copy.deepcopy(lines)
    co2_scrubber_rating = get_rating(number_list, 0, "C02")
    
    #Convert the values from binary to intgers
    oxygen_generator_rating = int(oxygen_generator_rating, 2)
    co2_scrubber_rating = int(co2_scrubber_rating, 2)
    
    #Multiply the two ratings to get the solution
    print("Problem 2 Output:", oxygen_generator_rating * co2_scrubber_rating)
    
problem2()