#day 4
print("--- Day 4: Giant Squid ---")

#                                   --- Problem 1 ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so 
# deep that you can't see any sunlight. What you can see, however, is a giant squid that 
# has attached itself to the outside of your submarine.
# Maybe it wants to play bingo?
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are 
# chosen at random, and the chosen number is marked on all boards on which it appears. 
# (Numbers may not appear on all boards.) If all numbers in any row or any column of a 
# board are marked, that board wins. (Diagonals don't count.)
# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid)
# pass the time. It automatically generates a random order in which to draw numbers and a 
# random set of boards (your puzzle input).
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked 
# numbers on that board.Then, multiply that sum by the number that was just called when the board won.
# To guarantee victory against the giant squid, figure out which board will win first. What will 
# your final score be if you choose that board?

def problem1():
    #Read input text
    input = open("input.txt")
    boards = input.read().split("\n\n")
    
    #Get the numbers drawed and remove them from the boards list
    numbers_drawed = boards.pop(0)
    numbers_drawed = numbers_drawed.split(",")

    #Make the boards a list of lists
    #Where boards[x] will be a list containing each row of board x
    for i in range(len(boards)):
        #Get the board and split it up by row
        board = boards[i]
        board = board.split("\n")
        #For each row remove replace any double spaces ('  ') with a single space (' ')
        for j in range(len(board)):
            row = board[j]
            board[j] = ' '.join(row.split())
        #Replace the board in lines with the new board
        boards[i] = board

    # Create a list of list where board_cols_rows[x] will be a list of 
    # sets representing the rows and columns in board x
    board_cols_and_rows = [[] for _ in range(len(boards))]
    # Iterate through each board to populate the list of rows and columns
    for i in range(len(boards)):
        board = boards[i]
        #Create a rows and columns list to hold lists of all 5 rows and 5 columns
        rows = []
        cols = [[] for _ in range(5)]
        #Iterate through each row of the bingo board
        for board_row in board:
            #Convert board_row from a list to a string
            board_row = board_row.split(" ")   
            #Add row to list of rows in the board  
            rows.append(board_row)
            #Iterate through the values in the row              
            for k in range(len(board_row)):     
                #Get the number
                number = board_row[k]         
                #Add the number to the correct column in the list of columns  
                cols[k].append(number)        
        #Now that we have a list of rows and list of column for this board turn them to 
        # sets and add them to the approiate list in boards_cols_and_rows     
        for j in range(len(rows)):
            row = set(rows[j])
            col = set(cols[j])

            board_cols_and_rows[i].append(row)
            board_cols_and_rows[i].append(col)

    #Need to take the first five drawn number and add to a set
    last_number_drawed = 0
    numbers_drawed_in_order = set()
    for i in range(5):
        #Get number drawed and add it to the set
        drawed_number = numbers_drawed[i]
        numbers_drawed_in_order.add(drawed_number)
        #Set the last number called
        if i == 4:
            last_number_drawed = drawed_number
    
    
    #Now need to check if there have been any rows or columns completed
    bingo = False
    for i in range(5,len(numbers_drawed)):
        #If bingo was found don't draw anymore numbers 
        if bingo == True:
            break
        #Iterate through each list holding the sets for columns and rows 
        for j in range(len(board_cols_and_rows)):
            board = board_cols_and_rows[j]
            #iterate through each set which represents a row or column in board j
            for row_or_col in board:
                #If found bingo no need to iterate thorugh any more rows or columns
                if bingo == True:
                    break
                #Get the intersetion of drawed numbers and row or column
                intersection = numbers_drawed_in_order.intersection(row_or_col)
                #If the intersection set has 5 elements that means that the row or column is fully marked
                if len(intersection) == 5:
                    bingo = True

            #If bingo was found need to mutiply sum of unmarked numbers and last number called
            if bingo == True:
                #Convert the board list to a single list holding all values
                board_single_list = [item for sublist in board for item in sublist]
                #Conveert list to a set
                board_single_set = set(board_single_list)
                #Get the difference so the new set only contains the unmarked numbers
                unmarked_numbers = board_single_set.difference(numbers_drawed_in_order)
                #Sum all the values in the set
                unmarked_sum = 0
                for number in unmarked_numbers:
                    number = int(number)
                    unmarked_sum += number
                #Calculate the solution and print
                print("Problem 1 output:", unmarked_sum * int(last_number_drawed))
                break
            else:
                #If bingo was not found get next number drawed and add it to the set
                next_number_drawed = numbers_drawed[i]
                numbers_drawed_in_order.add(next_number_drawed)
                #Update the new number to the last number called 
                last_number_drawed = next_number_drawed
problem1()

#                                     --- Problem 2 ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.
# You aren't sure how many bingo boards a giant squid could play at once, so rather than 
# waste time counting its arms, the safe thing to do is to figure out which board will win
# last and choose that one. That way, no matter which boards it picks, it will win for sure.
# Figure out which board will win last. Once it wins, what would its final score be?

def problem2():
    #Read input text
    input = open("input.txt")
    boards = input.read().split("\n\n")
    
    #Get the numbers drawed and remove them from the boards list
    numbers_drawed = boards.pop(0)
    numbers_drawed = numbers_drawed.split(",")

    #Make the boards a list of lists
    #Where boards[x] will be a list containing each row of board x
    for i in range(len(boards)):
        #Get the board and split it up by row
        board = boards[i]
        board = board.split("\n")
        #For each row remove replace any double spaces ('  ') with a single space (' ')
        for j in range(len(board)):
            row = board[j]
            board[j] = ' '.join(row.split())
        #Replace the board in lines with the new board
        boards[i] = board

    # Create a list of list where board_cols_rows[x] will be a list of 
    # sets representing the rows and columns in board x
    board_cols_and_rows = [[] for _ in range(len(boards))]
    # Iterate through each board to populate the list of rows and columns
    for i in range(len(boards)):
        board = boards[i]
        #Create a rows and columns list to hold lists of all 5 rows and 5 columns
        rows = []
        cols = [[] for _ in range(5)]
        #Iterate through each row of the bingo board
        for board_row in board:
            #Convert board_row from a list to a string
            board_row = board_row.split(" ")   
            #Add row to list of rows in the board  
            rows.append(board_row)
            #Iterate through the values in the row              
            for k in range(len(board_row)):     
                #Get the number
                number = board_row[k]         
                #Add the number to the correct column in the list of columns  
                cols[k].append(number)        
        #Now that we have a list of rows and list of column for this board turn them to 
        # sets and add them to the approiate list in boards_cols_and_rows     
        for j in range(len(rows)):
            row = set(rows[j])
            col = set(cols[j])

            board_cols_and_rows[i].append(row)
            board_cols_and_rows[i].append(col)

    #Need to take the first five drawn number and add to a set
    last_number_drawed = 0
    numbers_drawed_in_order = set()
    for i in range(5):
        #Get number drawed and add it to the set
        drawed_number = numbers_drawed[i]
        numbers_drawed_in_order.add(drawed_number)
        #Set the last number called
        if i == 4:
            last_number_drawed = drawed_number

    #Now need to check if there have been any rows or columns complpete
    #Create a list to hold boards the have bingo
    bingo_boards = []
    #Keep adding numbers to number drawed until all board have bingo
    for i in range(5,len(numbers_drawed)):
        #Iterate through all boards in boards cols and rows
        for j in range(len(board_cols_and_rows)):
            #Reset bingo
            bingo = False
            #Get board
            board = board_cols_and_rows[j]
            #Check for every set to see if there is a complete set
            for row_or_col in board:
                #Create a new set which is the intersection of numbers drawed and the row or col 
                intersection = numbers_drawed_in_order.intersection(row_or_col)
                #If the intersection is length of five it means a complete row or column
                if len(intersection) == 5:
                    bingo = True
            
            if bingo:
                #Remove board from board_rows_and_columns so it cant be called for bingo again
                board_cols_and_rows[j] = []
                #Add board to bingo boards
                bingo_boards.append(boards[j])
                #Check if the bingo board is the last board
                if len(bingo_boards) == len(boards):
                    #Convert the board list to a single list holding all values
                    board_single_list = [item for sublist in board for item in sublist]
                    #Conveert list to a set
                    board_single_set = set(board_single_list)
                    #Get the difference so the new set only contains the unmarked numbers
                    unmarked_numbers = board_single_set.difference(numbers_drawed_in_order)
                    #Sum all the values in the set
                    unmarked_sum = 0
                    for number in unmarked_numbers:
                        number = int(number)
                        unmarked_sum += number
                    #Calculate the solution and print
                    print("Problem 2 Output:", unmarked_sum * int(last_number_drawed))
                    break
        
        #If bingo was not found get next number drawed and add it to the set
        next_number_drawed = numbers_drawed[i]
        numbers_drawed_in_order.add(next_number_drawed)
        #Update the new number to the last number called 
        last_number_drawed = next_number_drawed
        
problem2()
