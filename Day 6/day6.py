#day6
print("--- Day 6: Lanternfish ---")

#                               --- Problem 1 ---
# The sea floor is getting steeper. Maybe the sleigh keys got carried this way?
# A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly?
# You should model their growth rate to be sure.
# Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each 
# lanternfish creates a new lanternfish once every 7 days.
# However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it 
# creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number 
# of days until it creates a new lanternfish.
# Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two 
# more days for its first cycle.
# So, suppose you have a lanternfish with an internal timer value of 3:
#       - After one day, its internal timer would become 2.
#       - After another day, its internal timer would become 1.
#       - After another day, its internal timer would become 0.
#       - After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
#       - After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal 
#         timer of 7.
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value). 
# The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.

def problem1():
    #Get the input internal_timers 
    input = open("input.txt")
    internal_timers = input.read().split(",")

    # Intialize day to day 1 
    day = 1
   
    # Update list until we reach day 80 
    while day < 81:
        #Reset the number of new fish
        new_fish = 0
        #Iterate though the internal timers
        for i in range(len(internal_timers)):
            # Get the internal timer
            internal_timer = int(internal_timers[i])
            # If an internal timer is equal to 0 increment the number of new fish and reset the value to 6
            if internal_timer == 0:
                new_fish += 1
                internal_timers[i] = 6
            #Otherwise decrement the internal timer
            else:
                internal_timers[i] = int(internal_timers[i]) - 1
        
        #For every new fish add an 8 to the list to represent a new internal timer
        for j in range(new_fish):
            internal_timers.append(8)
        
        #Increment the day
        day +=1

    #To get the solution get the length of internal timers
    print("Problem 1 Output:", len(internal_timers))

problem1()

#                                   --- Problem 2 ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
# How many lanternfish would there be after 256 days?
# **** Problem 1 solution was not efficent enough, needed to come up with a more efficent solution ****


def problem2():
    # Get the input internal_timers
    input = open("input.txt")
    data = input.read().split(",")

    #Create a list of 9 zeros to represent the 9 (0,1,2,3,4,5,6,7,8) different possible position in the timer
    internal_timers = [0] * 9
    
    #From the orginial list of timers get how many of each position exist and add that value to internal timer
    for i in range(len(internal_timers)):
        internal_timers[i] = data.count(str(i))

    #Intialize day
    day = 1

    #While day is less then 256 we will update the timers
    while day < 257:
        # The number of new fish to add after eaxh day will be the number of timers equal to 0
        new_fish = internal_timers[0]

        #Iterate through each position in internal timer except the last position
        for i in range(len(internal_timers)-1):
            #Update the number of timers at position i to the number of timers at position i + 1
            internal_timers[i] = internal_timers[i+1]

        # Set the value at position 8 to the number of new fish, which is the number of timers at value 0 the day before
        internal_timers[8] = new_fish
        #Also add the number of new fish to position 6 which represents fish restarting their timer
        internal_timers[6] += new_fish

        #increment the day
        day += 1

    #Sum up the values at each position to get the total number of fish
    sum = 0
    for i in range(len(internal_timers)):
        sum += internal_timers[i] 

    print("Problem 2 Output:", sum)    
    
problem2()