import collections
import math
#Day 14
print("--- Day 14: Extended Polymerization ---")

#                                               --- Problem 1 ---
# The incredible pressures at this depth are starting to put a strain on your submarine. The submarine 
# has polymerization equipment that would produce suitable materials to reinforce the submarine, and the 
# nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.
# The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers
# a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what
# polymer would result after repeating the pair insertion process a few times.
# The first line is the polymer template - this is the starting point of the process.
# The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and 
# B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.
# Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because 
# all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.
# Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

def problem1():
    #Read the input
    input = open("input.txt")
    data = input.read().split("\n\n")

    #Get the template
    template = data[0]

    #Create a dictionary for the pair insertions
    pair_insertions = {}
    #Iterate trhough each insertion
    for insertion in data[1].split("\n"):
        #Split inserttion by pair and element to insert
        insertion = insertion.split(" -> ")
        pair = insertion[0]
        element_insert = insertion[1]

        #Add pair insertion to the dictionary
        pair_insertions[pair] = element_insert

    #Intialize step and keep stepping until we reach step 10
    step = 1
    while step < 11:
        #Create a new template
        new_template = []
        #Iterate through the pairs in the template
        for i in range(len(template) - 1):
            #Get the pair at location i
            pair = template[i] + template[i+1]

            #Add element at location i and then the new element to be inserted from the pair
            new_template.append(template[i])
            new_template.append(pair_insertions.get(pair))
        
        #Add the last element in the orginail template to the new template
        new_template.append(template[-1])
        
        #Set the template to the new template and increment step
        template = new_template
        step += 1
    
    #Once have completed the ten steps get the count of the most common and least common element
    most_common_list = collections.Counter(template).most_common()
    most_common_element_count = most_common_list[0][1]
    least_common_element_count = most_common_list[-1][1]

    #Calculate the solution and print
    solution = most_common_element_count - least_common_element_count
    print("Problem 1 Output:", solution)


problem1()

#                                           --- Problem 2 ---
# The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to
# run more steps of the pair insertion process; a total of 40 steps should do it.
# Apply 40 steps of pair insertion to the polymer template and find the most and least common
# elements in the result. What do you get if you take the quantity of the most common element
# and subtract the quantity of the least common element?

def problem2():
    #Read the input
    input = open("input.txt")
    data = input.read().split("\n\n")

    #Get the template
    template = data[0]

    #Create a dictionary for the pair insertions
    pair_insertions = {}
    #Iterate trhough each insertion
    for insertion in data[1].split("\n"):
        #Split inserttion by pair and element to insert
        insertion = insertion.split(" -> ")
        pair = insertion[0]
        element_insert = insertion[1]

        #Add pair insertion to the dictionary
        pair_insertions[pair] = element_insert

    #Create a pair counter dictonary
    #Where the keys are the current pairs in the template and the value is the number of times the pair is in template
    pairs_counter = {}
    for i in range(len(template) - 1):
        #Get pair form template
        pair = template[i] + template[i+1]

        #If pair is already in the counter increment its counter
        if pair in pairs_counter:
            pairs_counter[pair] += 1
        #otherwise add it with a count value of 1
        else:
            pairs_counter[pair] = 1


    #Intialize step and keep stepping until we reach step 40
    step = 1
    while step < 41:
        #intialixe new pair counter
        new_pairs_counter = {}

        #Iterate through the pairs in the pairs_counter
        for pair in pairs_counter:
            #Get the number of pairs that are of this type of pair
            number_of_pair = pairs_counter[pair]
            #Get insertion character for this type of pair
            insertion_element = pair_insertions[pair]

            #Create two new pairs using the insertion character
            new_pair1 = pair[0] + insertion_element
            new_pair2 = insertion_element + pair[1]

            #If the first new pair is already in the new pair counter increment its counter value
            if new_pair1 in new_pairs_counter:
                new_pairs_counter[new_pair1] += number_of_pair
            #otherwise add it with a counter value equal to number of pair of orginial tyoe was
            else:
                new_pairs_counter[new_pair1] = number_of_pair
            
            #Do the same for second new pair
            if new_pair2 in new_pairs_counter:
                new_pairs_counter[new_pair2] += number_of_pair
            else:
                new_pairs_counter[new_pair2] = number_of_pair
            
        #Set the pairs_counter to the new pairs counter and increment step
        pairs_counter = new_pairs_counter
        step += 1
    
    #Create an elemnt counter to iterate throuhg all the pairs and add counter the number of times each elemnt appears
    element_counter = {}
    for pair in pairs_counter:
        #Get the two elements from the pair
        element1 = pair[0]
        element2 = pair[1]

        #If element exits in the counter increment the counter by the number of pairs there was
        if element1 in element_counter:
            element_counter[element1] += pairs_counter[pair]
        #Otherwise add the element and set the counter to the number of pairs there was
        else:
            element_counter[element1] = pairs_counter[pair]

        #Do the same for element two
        if element2 in element_counter:
            element_counter[element2] += pairs_counter[pair]
        else:
            element_counter[element2] = pairs_counter[pair]

    #Get the count of the most common element and the count of the least common element
    #Divide the values by two since when counting we actually counted for each element twice
    #Since the same element is actually associated with two different pairs
    most_common_element = math.ceil(max(element_counter.values())/2)
    least_common_element = math.ceil(min(element_counter.values())/2)
    
    #Caluclate the solution
    solution = most_common_element - least_common_element
    print("Problem 2 Output:", solution) 

problem2()
