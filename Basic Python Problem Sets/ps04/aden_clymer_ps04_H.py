###################################################
# Coder: Aden Clymer
# Assignment: Problem Set 4
# Date: 2 October 2023
###################################################
import doctest
import math
import random
import datetime

# Define a function named check_file with two parameters, both strings. 
# The first string represents a filename and the second a word. 
# The function should read the contents of the file and count how many times the word appears in the file. 
# The function should count all instances of the word (see examples below). 
# Return the number of times the word appears in the file as integer. Assume the file exists.

def check_file(my_file, word: str) -> int:
    '''
    # >>> check_file('word_0.txt', 'word')
    # 0
    # >>> check_file('word_1.txt', 'Word')
    # 1
    # >>> check_file('word_3.txt', 'time')
    # 3
    '''
    count: int = 0 #start count as zero
    small_word:str = word.lower() #Making all strings lowercase to utilize for comparisons
    with open(my_file, "r") as f: #iterate through the file and read it
        for line in f:
            small_line:str = line.lower()
            for i in range(len(small_line)-len(small_word)): #basically if the word exists in the line, the count goes up by one
                if small_word == small_line[i:i+len(small_word)]:
                    count+=1
    return count 


# Define a function named most_expensive_order with one parameter, a string.
# The string represents a filename. 
# The file contains customer orders from a local coffee shop. 
# each line in the file represents a different order 
#   (e.g. LCMM is a customer who ordered 1 Latte, 1 Coffee, and 2 Muffins). 
# The function should determine the most expensive customer order and return the string that describes
# that order. 
# Assume the file exists and contains only valid characters 
#   (e.g. 'CLPOM/n' where '/n' is the newline character at the end of the line).
def most_expensive_order(filename: str) -> str:
    '''
    #>>> most_expensive_order('coffee0.txt')
    #'PO'
    #>>> most_expensive_order('coffee1.txt')
    #'CCPMCCOL'
    '''
    #the menu
    coffee: float = 2.50
    latte: float = 3.25
    cappuccino: float = 3.50
    croissant: float = 2.75
    muffin: float = 2.00

    #setting up some variables
    highest_choice = 0
    best_combination:str = ""

    with open(filename) as f: 
        for letter in f:
            #every line reset the num of items to zero
            num_coffees = num_latte = num_cap = num_crois = num_muffin = total_price = 0
            #if the letter exists, the count will be added to the number
            for i in range(len(letter)):
                if letter[i] == "C":
                    num_coffees += 1
                if letter[i] == "L":
                    num_latte += 1
                if letter[i] == "P":
                    num_cap += 1
                if letter[i] == "O":
                    num_crois += 1
                if letter[i] == "M":
                    num_muffin += 1
            #calculating the num of items by the price to find out the total
            total_price = ((coffee*num_coffees)+(latte*num_latte)+(cappuccino*num_cap)+(croissant*num_crois)+(muffin*num_muffin))
            #print(letter) # code for checking myself
            #print(total_price) # code for checking myself
            
            #if a line's total price was higher than the previous highest value, then it becomes the new value
            if total_price > highest_choice:
                highest_choice = total_price
                best_combination = letter.replace("\n","")
    return best_combination

# Write a Python function named find_waldo 
# The function should take one parameter, a string representing the name of a file. 
# The function should read the contents of the file and return 5-digit zip code (as a string).
# Here are the specifics of Waldo's hiding strategy:
#       Waldo's name, 'Waldo', will appear exactly once in the text file.
#       Immediately after 'Waldo', there will be a space, followed by a hidden 5-digit zip code.
#       The zip code is represented by five consecutive digits with no spaces in between.
#       Waldo ensures that this pattern occurs only once in the entire file.
# If there are any deviations from this pattern, the function should return the
# string 'Waldo is missing!' to indicate that Waldo's location could not be found.
def find_waldo(filename:str)->str:
    '''
    >>> find_waldo('waldo_location.txt')
    '12345'
    >>> find_waldo('missing_location.txt')
    'Waldo is missing!'
    '''
    try: 
        #setting code up expecting if statements to be a failure
        where_waldo: str = "Waldo is missing!"
        with open(filename, "r") as f:
            for line in f:
                #print(line) #to check myself

                #if waldo is in a line this section of code will run through and see if there are 5 digits after his name
                if ("Waldo" in line):
                    #print(line) #to check myself
                    start_name = line.index("Waldo")
                    start_digits = start_name+6
                    #print(line[start_name:start_digits]) #to check myself
                    if line[start_digits:start_digits+5].isdigit():
                        where_waldo = line[start_digits:start_digits+5]
        return where_waldo
    except FileNotFoundError as e:
        print(e+": File does not exist")        



# Define a procedure named update_log that has one parameter, a string.
# The string will contain the most recent event that needs to be added to the log file.
# Your procedure should append the provided string to the existing
# server_status.log file. Assume the file exists.
def update_log(update:str)->str:
    '''
    >>> fd = open('server_status.log', 'w')
    >>> fd.write('2023-09-19 16:00:17 - WARNING - This is a warning message.\\n')
    59
    >>> fd.close()
    >>> update_log('2023-09-19 16:00:23 - INFO - This is an information message.')
    >>> fd = open('server_status.log', 'r')
    >>> test_file_contents = fd.read()
    >>> fd.close()
    >>> fd = open('actual_server_status.log', 'r')
    >>> truth_file_contents = fd.read()
    >>> fd.close()
    >>> truth_file_contents == test_file_contents
    True
    '''
    #initialzing a list to append to
    server_contents = []
    with open("server_status.log", "r") as f:
        #stocking up the list with everything from the log
        for line in f: 
            message = line
            server_contents.append(message)
        
        #now writing over the file I just iterated through with the same content along with the new content
        with open("server_status.log", "w") as g:
            server_contents.append(update)
            for j in server_contents:
                g.write(j)
                #print(j) #to check myself

    

# Define a procedure named check_homework that has one parameter, 
#   a string that represents the name of a student’s homework file.
# Grade text files that second-grade students submitted. 
# Their assignment was to write words that started with the specified letter and length. 
# Your procedure should save the output to a feedback file. 
# The name of the feedback file should be the name of the original file with _feedback appended. 
#   (e.g. If the original file name is fred.txt the feedback file is fred_feedback.txt) 
# The feedback file should contain one line for each entry in the original file. 
# The line should indicate if the word is correct or wrong:
#   If the letter and length match the word provided the feedback includes both
#       the letter and the length and the word Correct (e.g., A8 Correct because
#       aardvark starts with A and is eight letters).
#   If the line was incorrect, the incorrect letter and/or length is replaced by
#       hyphens and the line is indicated as wrong. (e.g., T- Wrong because Turnip
#       tarts with T, but it isn’t three letters).
# Assume spelling is correct for all words.
# A8 Correct
# T- Wrong
# H5 Correct
# -8 Wrong
# -- Wrong
def check_homework(hw_file:str):
    '''
    >>> check_homework('elend.txt')
    >>> fd = open('elend_feedback.txt', 'r')
    >>> test_file_contents = fd.read()
    >>> fd.close()
    >>> fd = open('actual_elend_feedback.txt', 'r')
    >>> truth_file_contents = fd.read()
    >>> fd.close()
    >>> truth_file_contents == test_file_contents
    True
    '''
    try:
        list_for_file = []
        new_hw_file = hw_file.replace(".txt","_feedback.txt")
        with open(hw_file, "r") as f:
            i = 0
            for line in f:
                #print(line)
                
                #Set up comparison statments
                nude_line = line.strip()
                seperated_line = nude_line.split(":")
                checker = seperated_line[0] #assistance from Beck
                student = seperated_line[1] #Assitance from Beck
                feedback = "" #Assistance from Beck
                
                #compare and see if the values are right or wrong
                if checker[0].lower() == student[0].lower() and int(checker[1]) == len(student):
                    feedback = checker + " Correct"
                elif checker[0].lower() != student[0].lower():
                    checker = "-" + checker[1:]
                    feedback = checker + " Wrong"
                elif int(checker[1]) != len(student):
                    checker = checker[0]+"-"
                    feedback = checker + " Wrong"
                list_for_file.append(feedback)

        #write a file that has all the grades written as right or wrong
        with open(new_hw_file, "w") as g:
            for j in list_for_file:
                g.write(j+"\n")
                #print(j)
    except FileNotFoundError as e:
        print(e+": File does not exist")


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)