#day 12
print("--- Day 12: Passage Pathing ---")

#                                       --- Problem 1 ---
# With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of 
# this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found 
# the best path is to find all of them.
# Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input).
# This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave 
# named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.
# Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once.
# There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would
# be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them 
# multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.
#How many paths through this cave system are there that visit small caves at most once?

#Depth first search algorithm used to find all possible paths
def dfs(graph, start, end, visited, path, all_paths):

    #If the current cave is lower case mark it as visited as it is a small cave and we can onyl visit it once
    if start.islower():
        visited.append(start)
    #Add cave to our path
    path.append(start)

    #If this cave is the end cave add the path to our list of possible path
    if start == end:
        all_paths.append(path)
    #Otheriwse call depth first search from this new cave
    else:
        #Get possible paths
        possible_paths = graph.get(start)
        #Iterate through paths calling depth first search if cave was not already viistied
        for possible_path in possible_paths:
            if not possible_path in visited:
                dfs(graph, possible_path, end, visited, path, all_paths)
    
    #Once if completed all possibilities remove cave form path and remove it from visited list if it is a small cave
    path.pop()
    if start.islower():
        visited.remove(start)


def problem1():
    #Get the input
    input = open("input.txt")
    lines = input.read().split("\n")

    #Create a dictonary of all caves and the caves you can access from that cave
    #{'A': ['b', 'd']} would reprsent cave A and b and d would be the caves you can access from A
    all_caves = {"start": []}

    #Iterate throuhg each line in the input
    for line in lines:
        #Get the two caves
        caves = line.split("-")
        cave1 = caves[0]
        cave2 = caves[1]

        #If there is already a key for cave1 add caved 2 as a possible path
        if cave1 in all_caves:
            cave_routes = all_caves.get(cave1)
            cave_routes.append(cave2)
        #Otherwise create a new key and add cave2 as a path
        else:
            all_caves[cave1] = [cave2]
        
        #Do the same for cave 2
        if cave2 in all_caves:
            cave_routes = all_caves.get(cave2)
            cave_routes.append(cave1)
        else:
            all_caves[cave2] = [cave1]

    #Intialize empty list of visited, path, and all possible paths
    visited = []
    path = []
    all_paths = []
    #Call dfs from 'start' cave and make the 'end' cave the final destination
    dfs(all_caves, "start", "end", visited, path, all_paths)


    
    #Print the length of the possible paths
    print("Problem 1 Output:", len(all_paths))

problem1()

#                                           --- Problem 2 ---
# After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, 
# big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small
# caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you
# leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.
# Given these new rules, how many paths through this cave system are there?

#Depth first search algorithm used to find all possible paths for problem 2
def dfs_2(graph, start, end, visited_once, visited_twice, path, all_paths, small_cave_visited_twice):
    #If start cave equals "start" or "end" add to visited_twice
    #We only want to visit 'start' or 'end' once. So by adding to visited_twice right away we can not access them again
    if start == "start" or start == "end":
        visited_twice.append(start)

    #If the current cave is lower case then we need to increment its counter and add it to a visited list based on its counter
    elif start.islower():
        graph[start + "_counter"] += 1
        #If cave was not visited twice add it to visited once list
        if graph[start + "_counter"] == 1:
            visited_once.append(start)
        #If visited twice add to visited twice list and set small cave visited twice variable to True
        elif graph[start + "_counter"] == 2:
            small_cave_visited_twice = True
            visited_twice.append(start)
    
    #Add cave to our path
    path.append(start)

    #If this cave is the end cave add the path to our list of possible path
    if start == end:
        all_paths.append(path)
    #Otheriwse call depth first search from this new cave
    else:
        #Get possible paths
        possible_paths = graph.get(start)
        #Iterate through paths calling depth first search
        for possible_path in possible_paths:
            #If cave is not in visited_twice list continue
            if not possible_path in visited_twice:
                #If a small cave has been visited twice we need to check if the possible path is in visited_once list
                #If not has been visited once call depth first search from this cave
                if small_cave_visited_twice:
                    if not possible_path in visited_once:
                        dfs_2(graph, possible_path, end, visited_once, visited_twice, path, all_paths, small_cave_visited_twice)
                #Otherwise we have not entered any small caves yet so we can enter any cave 
                else:
                    dfs_2(graph, possible_path, end, visited_once, visited_twice, path, all_paths, small_cave_visited_twice)

    
    #Once completed pop cave from path
    path.pop()

    #If cave was a smaller cave we need to remove it form the visited list
    if start.islower():
        #If it was the 'start' cave or 'end' cave remove it from visited_twice list
        if start == "start" or start == "end":
            visited_twice.remove(start)
        #If it is a small cave that was not 'start' or 'end'
        else:
            #Decrement counter
            graph[start + "_counter"] -= 1
            #If in visited_twice remove it 
            if start in visited_twice:
                visited_twice.remove(start)
            #Otherwise it had to be in visited_once so remove it
            else:
                visited_once.remove(start)

def problem2():
    #Get the input
    input = open("input.txt")
    lines = input.read().split("\n")

    #Create a dictonary of all caves and the caves you can access from that cave
    #{'A': ['b', 'd']} would reprsent cave A and b and d would be the caves you can access from A
    all_caves = {"start": []}

    #Iterate throuhg each line in the input
    for line in lines:
        #Get the two caves
        caves = line.split("-")
        cave1 = caves[0]
        cave2 = caves[1]

        #If there is already a key for cave1 add caved 2 as a possible path
        if cave1 in all_caves:
            cave_routes = all_caves.get(cave1)
            cave_routes.append(cave2)
        #Otherwise create a new key and add cave2 as a path 
        else:
            all_caves[cave1] = [cave2]
            #Also create a cave counter to keep track of how many times a cave is enetered
            all_caves[cave1 + "_counter"] = 0
        
        #Do the same for cave 2
        if cave2 in all_caves:
            cave_routes = all_caves.get(cave2)
            cave_routes.append(cave1)
        else:
            all_caves[cave2] = [cave1]
            #Also create a cave counter to keep track of how many times a cave is enetered
            all_caves[cave2 + "_counter"] = 0


    #Intialize empty list of visited_once, visited_twice, path, and all possible paths, and variable to keep track if a msall cave was visited twice
    visited_once = []
    visited_twice = []
    path = []
    all_paths = []
    small_cave_visited_twice = False
    #Call dfs from 'start' cave and make the 'end' cave the final destination
    dfs_2(all_caves, "start", "end", visited_once, visited_twice, path, all_paths, small_cave_visited_twice)

    #Print the length of the possible paths
    print("Problem 2 Output:", len(all_paths))

problem2()