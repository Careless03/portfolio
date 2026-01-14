###################################################
# Coder: Aden Clymer
# Assignment: Problem Set 5
# Date: 9 October 2023
###################################################
import doctest
# Define a function named make_word_list that has two parameters, a string
# and an integer. The string represents the name of a file. If the file exists, the
# function should read the contents of the file and return a list of the words in
# the file whose length is greater than or equal to n. If the file does not exist
# return the string: '{filename} not found.' Where the {filename} is replaced
# with the name of the file that is not found. If the file exists, you can assume
# that there will be one word per line.
def make_word_list(filename:str, number:int)->list:
    '''
    >>> make_word_list('words.txt', 4)
    ['moon', 'fish', 'ball', 'book', 'tree', 'bird']
    >>> make_word_list('words.txt', 5)
    []
    >>> make_word_list('file_does_not_exist.txt', 5)
    'file_does_not_exist.txt not found.'
    '''
    try:
        with open(filename,"r") as f: #opens a file and reads it
            num_words:list = [] #creates a blank list
            for line in f:
                line = line.removesuffix("\n")
                if len(line) >= number: 
                    num_words.append(line)
        return num_words
    except FileExistsError and FileNotFoundError:
        return filename+ " not found."
# Write a function named average_word_length which takes one argument, a
# list of strings. The function calculates and returns the average length of the
# strings in the list.
def average_word_length(list_of_words: list)->int:
    '''
    >>> x = average_word_length(['book', 'xylophone', 'treehouse', 'aardvark'])
    >>> abs(x - 7.5) < 0.000001
    True
    '''
    total_length: int = 0
    try:
        for word in range(len(list_of_words)): #iterates through the length of the list
            total_length += len(list_of_words[word]) #finds the total length of all words combined
    except TypeError as e:
        print(e+" that is not the correct type")
    return total_length/(len(list_of_words))
# Define a function named check_grades with one parameter, a list of floats. The
# list of floats represents grades. All grades should be floating point values in the
# range [0.0, 100.0]. Your function should verify that the values in the list are in
# the specified range (0.0 ≤ grade ≤ 100.0). If all the grades are within the
# specified range return the string 'Grades Validated' otherwise raise a value
# error with the message 'Invalid Grade(s)'.
# Note: This problem is specifically designed to assess your ability to raise an
# error. Normally, when we raise an error, we also want to handle that error and
# ensure our program doesn’t crash
def check_grades(list_of_grades: float):
    '''
    >>> check_grades([10.0, 100.0, 77.5])
    'Grades Validated'
    >>> check_grades([10.0, 100.0, -7.5])
    Traceback (most recent call last):
    ...
    ValueError: Invalid Grade(s)
    '''
    grades_validated = True
    for grade in range(len(list_of_grades)):
        print(list_of_grades[grade]) #checker for me
        if int(list_of_grades[grade]) < 0.0 or int(list_of_grades[grade]) > 100.0:
            print(list_of_grades[grade]) #checker for me
            grades_validated = False
            raise ValueError("Invalid Grade(s)") #raises an error value
    if grades_validated == True:
        return "Grades Validated"
# Define a function named get_ACFT_stats with one parameter, a list containing
# your Soldiers’ ACFT scores. You want to calculate the min, max, and average
# scores for your platoon. However, there is a complication: some of the Soldiers
# in your platoon did not take the ACFT, and their scores are marked as None in
# the list. Your function needs to calculate and return the minimum, maximum,
# and average ACFT scores, while excluding the None scores from the calculation.
# The average score should be rounded down to the nearest integer.
# Note: None does not have quotations because it is not a string. It is the sole
# instance of the NoneType type and is frequently used to represent the absence
# of a value.
def calc_average(a_list:list)->int: #helper function that calcs the avg
    total = 0 #initiazes the total as 0 or resets it
    for i in range(len(a_list)):
        total += int(a_list[i])
    return total/len(a_list)

def get_ACFT_stats(acft_scores:list):
    '''
    >>> get_ACFT_stats([380, 550, 575])
    (380, 575, 501)
    >>> get_ACFT_stats([400, 500, 600])
    (400, 600, 500)
    >>> get_ACFT_stats([400, 500, None, 600])
    (400, 600, 500)
    '''
    try:
        new_acft_scores: list = []
        for score in range(len(acft_scores)):
            if acft_scores[score] != None: #checks if there is a value named 'None'
                print(acft_scores[score])
                new_acft_scores.append(acft_scores[score])
            else:
                continue #if there is a value of None, pass by one iteration
            #print(new_acft_scores[score])
        minimum = int(min(new_acft_scores)) #finds the min value
        maximum = int(max(new_acft_scores)) #finds the max value
        average = int(calc_average(new_acft_scores)) #calls the function for the average value
        listings = (minimum,maximum,average) #creates a tuple based on the min, max, and avg
        return listings
    except ValueError as e:
        print(e+" that doesn't belong there silly")
# Define a function named calc_nums that takes one parameter, a tuple
# containing three numbers, and performs the following operation: first number
# in tuple is raised to the power of the second number in the tuple and the result
# is divided by the third number in the tuple.
# The function returns the result (a single number). Although the parameter of
# your function is supposed to be a tuple of three numbers, sometimes you may
# get a tuple that is not in accordance with specifications.
# Write your function so that it gracefully handles (does not crash) the following
# errors: ZeroDivisionError, IndexError and TypeError. If an error occurs during
# the execution of your function, return one of the following strings corresponding
# to the type of error encountered: 'Error: zero_division', 'Error: index', or
# 'Error: type'. You only need to check/handle these three types of errors. The
# provided doctests exemplify the different types of errors that can occur.
def calc_nums(numbers:tuple):
    '''
    >>> calc_nums((2, 2, 2))
    2.0
    >>> calc_nums((2, 2))
    'Error: index'
    >>> calc_nums((2, 2, 0))
    'Error: zero_division'
    >>> calc_nums((2, 2, '2'))
    'Error: type'
    '''
    try: #raises the first by the power of the second, divided by the power of the third
        result = float(((numbers[0]**numbers[1])/numbers[2])) #the only important thing 
        return result
    

    except ZeroDivisionError: #checks for dividing by zero
        return "Error: zero_division"
    except IndexError: #checks for indexing error
        return "Error: index"
    except TypeError:
        return "Error: type"
if __name__ == '__main__':
    doctest.testmod(verbose=True)