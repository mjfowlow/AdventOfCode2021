import math

#Day 10
print("--- Day 10: Syntax Scoring ---")

#                                   --- Problem 1 ---
# You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:
# Syntax error in navigation subsystem on line: all of them
# All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).
# The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, 
# and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, 
# the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching brackets:
#       - If a chunk opens with (, it must close with ).
#       - If a chunk opens with [, it must close with ].
#       - If a chunk opens with {, it must close with }.
#       - If a chunk opens with <, it must close with >.
# So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, 
# [<>({}){}[([])<>]], and even (((((((((()))))))))).
# Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.
# A corrupted line is one where a chunk closes with the wrong bracket - that is, where the brackets it opens and closes with 
# do not form one of the four legal pairs listed above.
# Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, 
# and its presence causes the whole line to be considered corrupted.
# Stop at the first incorrect closing bracket on each corrupted line.
# Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! 
# To calculate the syntax error score for a line, take the first illegal bracket on the line and look it up in the following table:
#       - ): 3 points.
#       - ]: 57 points.
#       - }: 1197 points.
#       - >: 25137 points.
# Find the first illegal bracket in each corrupted line of the navigation subsystem.
# What is the total syntax error score for those errors?

def problem1():
    #Read the input data
    input = open("input.txt")
    lines = input.read().split("\n")

    #Create a dictionary of the associated points and matching brackets
    points = {")": 3,  "]": 57, "}": 1197, ">": 25137 }
    bracket_matches = {"(":")", "[":"]", "{":"}", "<":">"}

    #Intialize total score to 0
    total_score = 0

    #Iterate throuhg each line
    for line in lines:
        #Intialize stack for line to hold open brackets
        open_char_stack = []

        # Iterate through each bracket
        for bracket in line:
            #Check if bracket is an opening bracket.
            #If it is add to the stack
            if bracket == "(" or bracket == "[" or bracket == "{" or bracket == "<":
                open_char_stack.append(bracket)
            
            #Got closing bracket
            else:
                #Pop from the stack to get the last opening bracket
                open_bracket = open_char_stack.pop(len(open_char_stack)-1)

                #Check if brackets match
                #If they don't add to the total score and move on to the next line
                if bracket_matches[open_bracket] != bracket:
                    total_score += points[bracket]
                    break

    print("Problem 1 Output:", total_score) 

problem1()

#                                   --- Problem 2 ---
# Now, discard the corrupted lines. The remaining lines are incomplete.
# Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the 
# end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters 
# that complete all open chunks in the line.
# You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal 
# pairs are formed and all chunks end up closed.
# Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion 
# string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and 
# then increase the total score by the point value given for the character in the following table:
#       - ): 1 point.
#       - ]: 2 points.
#       - }: 3 points.
#       - >: 4 points.
# Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. 
# (There will always be an odd number of scores to consider.)
# Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

def problem2():
    #Read the input data
    input = open("input.txt")
    lines = input.read().split("\n")

    #Create a dictionary of the associated points and matching brackets
    points = {")": 1,  "]": 2, "}": 3, ">": 4 }
    bracket_matches = {"(":")", "[":"]", "{":"}", "<":">"}

    #Intialize a list ot hold the socres of the incomplete lines
    scores = []

    #Iterate throuhg each line
    for line in lines:
        #Intialize stack for line to hold open brackets
        open_char_stack = []

        # Iterate through each bracket
        for i in range(len(line)):
            #Get bracket
            bracket = line[i]

            #Check if bracket is an opening bracket.
            #If it is add to the stack
            if bracket == "(" or bracket == "[" or bracket == "{" or bracket == "<":
                open_char_stack.append(bracket)
            
            #Got closing bracket
            else:
                #Pop from the stack to get the last opening bracket
                open_bracket = open_char_stack.pop(len(open_char_stack)-1)

                #Check if brackets match
                #If they don't add to the total score and move on to the next line
                if bracket_matches[open_bracket] != bracket:
                    break
            
            #If we are at the last bracket in the list and there are still brackets in the stack we need to add closng brackets
            if i == len(line) - 1 and len(open_char_stack) > 0:
                #Intialize score
                score = 0
                #While there are brackets in the stack add closing brackets
                while(len(open_char_stack) > 0):
                    #Get bracket from stack and get matching closing bracket
                    open_bracket = open_char_stack.pop(len(open_char_stack)-1)
                    close_bracket = bracket_matches[open_bracket]
                    #Multiply the score by 5 and add the points for the bracket added
                    score *= 5
                    score += points[close_bracket]
                
                #Add the score to the list of scores 
                scores.append(score)

    #Sort scores and get the middle one
    scores = sorted(scores)
    middle_score = scores[math.ceil(len(scores)/2) -  1]

    print("Problem 2 Output:", middle_score) 

problem2()