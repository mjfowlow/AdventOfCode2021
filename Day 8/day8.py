#Day 8
print("--- Day 8: Seven Segment Search ---")

#                                           --- Problem 1 ---
# You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. 
# Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.
# As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment 
# displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a 
# lot of trouble without them, so you'd better figure out what's wrong.
# Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g.
# So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f 
# would be turned on.
# The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying 
# to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. 
# Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display 
# use the same connections, though.)
# So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only 
# digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still 
# can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.
# For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then 
# write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which 
# pattern corresponds to which digit.
# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same 
# wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the
# ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that 
# uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit 
# that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.
# Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, 
# you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) 
# use five segments and are more difficult to deduce.
# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to 
# those digits. Counting only digits in the output values (the part after | on each line).
# In the output values, how many times do digits 1, 4, 7, or 8 appear?

def problem1():
    #Get the input
    input = open("input.txt")
    lines = input.read().split("\n")

    #Intialize the number of unique segments
    num_unique_segments = 0

    #iterate through the lines
    for line in lines:
        #Get the output values and make a list of the output values
        output_values = line.split(" | ")[1]
        output_values = output_values.split(" ")

        #Iterate through each value
        for value in output_values:
            #Get the length
            length_value = len(value)
            #If length equals any of the unique segments increment the unique segment counter
            if length_value == 2 or length_value == 4 or length_value == 3 or length_value == 7:
                num_unique_segments += 1
    
    #Print the solution
    print("Problem 1 Output:", num_unique_segments)

problem1()

#                                       --- Problem 2 ---
# Through a little deduction, you should now be able to determine the remaining digits.
# For each entry, determine all of the wire/segment connections and decode the four-digit output values. 
# What do you get if you add up all of the output values?

def problem2():
    #Get the input
    input = open("input.txt")
    lines = input.read().split("\n")

    #Intialize sum to 0
    sum_output_values = 0

    #iterate through each line
    for line in lines:

        #Get the signal patterns and the output values
        signal_patterns = line.split(" | ")[0].split(" ")
        output_values = line.split(" | ")[1].split(" ")

        #Get 1, 4, 7, 8, and possible two values
        possible_twos = []
        for pattern in signal_patterns:
            if len(pattern) == 2:
                one = set(pattern)
            elif len(pattern) == 3:
                seven = set(pattern)
            elif len(pattern) == 4:
                four = set(pattern)
            elif len(pattern) == 5:
                possible_twos.append(set(pattern))
            elif len(pattern) == 7:
                eight = set(pattern)
        
        #Set the top-right and bottom-right patterns equal to one, as they currently have two possible values
        top_right = one
        bottom_right = one

        #Get the top value by getting the difference in 7 and 1
        top = seven - one         

        #Set the possible values for center and top-left as the difference in 4 and 1
        top_left = four - one
        center = top_left

        #Iterate through the possible values for two and get rid of any values that contain 1 or both the center values
        for pattern in possible_twos:
            if not one.issubset(pattern) and not center.issubset(pattern):
                two = set(pattern)
                break 

        #Set bottom-right, top-right, center, and top-left
        bottom_right = one - two
        top_right = top_right - bottom_right
        top_left = top_left - two
        center = center - top_left

        #Only two possible values left for bottom-left and bottom, get them
        bottom_left = two - four - seven
        bottom = bottom_left    
        
        #Get 5
        possible_fives = possible_twos
        #Get rid of values that contain both bottom_left and bottom, and top_tight
        for pattern in possible_fives:
            if not bottom.issubset(pattern) and not top_right.issubset(pattern):
                five = pattern
                break
        #Get the bottom-left and bottom values
        bottom_left = bottom_left - five
        bottom = bottom - bottom_left

        #Creat 0, 3, 6, 9 by starting with eight and subrtacting the neccessary segments
        zero = eight - center
        three = eight - top_left - bottom_left
        six = eight - top_right
        nine = eight - bottom_left

        #Create a list to hold all numbers
        numbers = [zero, one, two, three, four, five, six , seven, eight, nine]

        #Get the output number
        output_number = ""
        for value in output_values:
            for i in range(len(numbers)):
                number = numbers[i]
                if set(value) == number:
                    output_number += str(i)

        #Add output value to the sum
        sum_output_values += int(output_number)
    
    #Print the solution
    print("Problem 2 output:", sum_output_values)

problem2()