##################################################
# Coder: Aden Clymer
# Assignment: Problem Set 6
# Date: 14 October 2023
###################################################
import doctest
import copy

# # Define a function named starts_with that accepts two strings as arguments:
# # the name of a file and a single character. Each line in the file contains a
# # single word. Return an alphabetically sorted list containing the words from
# # the file that start with the letter specified by the second argument. The 
# # file p1_example.txt is provided as an example. If the file does not exist 
# # return an empty list. You may assume all characters in the file and the 
# # letter passed in as an argument are lowercase.
def starts_with(filename:str, character:str)->list:
    """
    >>> starts_with('p1_example.txt', 's')
    ['schists', 'seriatim', 'shantung']
    >>> starts_with('NOT_p1_example.txt', 's')
    []
    >>> starts_with('p1_example.txt', 'x')
    []
    """
    
    try:
        with open(filename,"r") as f: #opens file
            selected_list:list = []
            
            # goes through each line and sees if the first part starts with 
            # the predetermiened character
            for line in f:
                line = line.strip()
                if line[0:len(character)] == character:
                    selected_list.append(line)
            
            # Alphabetizes the list
            selected_list.sort()
            return selected_list
    except IndexError as e:
        print(str(e)+": There were blank lines in your code.")
    except FileNotFoundError as e:
        bad_list = []
        print(bad_list)
    

# # Define a function named find_highest_avg_temperature with one
# # parameter, a string representing a file name. The file contains temperature
# # recordings for different cities. Each line in the file consists of the city
# # name followed by temperature recordings for several days, separated by 
# # commas. Your task is to read the data from the file and return the name of 
# # the city with the highest average temperature. Assume the file exists.

# # Helper function to find the average
# def find_average(a_list:list)->int:
#     for i in range(len(a_list)):
#         a_list[i] = int(a_list[i])
#     avg = sum(a_list)/len(a_list)
#     return avg

# def find_highest_avg_temperature(filename:str)->str:
#     """
#     >>> file_name = 'p2_example.txt'
#     >>> find_highest_avg_temperature(file_name)
#     'Los Angeles'
#     """
#     with open(filename) as f: 
#         avg_temp: int = 0
#         highest_city: str = ""
#         for line in f: 
#             nude_line:str = line.strip() #removes spaces
#             split_line:list = nude_line.split(",") #makes a list
#             #print(split_line) #testing
#             avg_list:list = copy.deepcopy(split_line) #makes a deepy copy
#             #print(avg_list[1:]) #testing
#             average = find_average(avg_list[1:])
#             #print(average) #testing

#             # gets the city with the highest avg temp
#             if average > avg_temp:
#                 highest_city = split_line[0]
#                 avg_temp = average
#         return highest_city


# Define a function named merge_and_sort_tuples with three parameters. The
# first two parameters are required; they are tuples containing integer values 
# and the optional parameter is a Boolean with the default value of True. The 
# function should merge the two tuples and sorts them either in ascending or 
# descending order based on the 3rd parameter. If the 3rd parameter is True, 
# the tuple should be sorted in ascending order. If the 3rd parameter is 
# False, the tuple should be sorted in descending order. Return the sorted 
# tuple. Assume only tuples containing integer values are passed into the 
# function.
def merge_and_sort_tuples(set_one:tuple,set_two:tuple,asc:bool = True)->tuple:
    """
    >>> tuple1 = (5, 3, 8, 2)
    >>> tuple2 = (9, 1, 6, 4)
    >>> merge_and_sort_tuples(tuple1, tuple2)
    (1, 2, 3, 4, 5, 6, 8, 9)
    >>> merge_and_sort_tuples(tuple1, tuple2, False)
    (9, 8, 6, 5, 4, 3, 2, 1)
    >>> merge_and_sort_tuples((), (), False)
    ()
    """
    full_list = []
    final_tuple = ()
    #make an adjustable list
    for i in range(len(set_one)):
        full_list.append(set_one[i])
    for j in range(len(set_two)):
        full_list.append(set_two[j])
    #create the code for ascending
    if asc:
        full_list.sort()
    #create the code for descending
    elif not asc:
        full_list.sort(reverse = True)
    final_tuple = tuple(full_list)
    return final_tuple
    

# # Define a function named sum_lists_at_index with two parameters, both of
# # which are lists of integers. The function's objective is to produce a new
# # list with a length equal to the longer of the two input lists. For each index
# # in the new list, calculate the sum of the corresponding elements from both
# # input lists. If one of the input lists is shorter than the other, treat the 
# # missing elements as if they were 0 for that list. Populate the new list with
# # the sums, and finally, return this resulting list. It's important to assume
# # that all non-empty lists will only contain integers.
def sum_lists_at_index(listA:list,listB:list):
    """
    >>> list1 = [1, 2, 3]
    >>> list2 = [4, 5, 6, 7]
    >>> sum_lists_at_index(list1, list2)
    [5, 7, 9, 7]
    >>> list1 = [1, 2, 3, 4, 5]
    >>> list2 = [4, 5, 6]
    >>> sum_lists_at_index(list1, list2)
    [5, 7, 9, 4, 5]
    >>> list1 = [1, 2, 3]
    >>> list2 = []
    >>> sum_lists_at_index(list1, list2)
    [1, 2, 3]
    """
    #find the difference in the lengths of the list
    difference = abs(len(listA)-len(listB))
     #make a copy so as to not mess up the first two lists
    copyA = copy.deepcopy(listA)
    # print(copyA)
    copyB = copy.deepcopy(listB)
    # print(copyB)

    # make both lists the same length
    if len(copyA)>=len(copyB):
        created_list:list = [0]*len(copyA)
        for j in range(difference):
            copyB.append(0)
    elif len(copyB)>len(copyA):
        created_list:list = [0]*len(copyB)
        for h in range(difference):
            copyA.append(0)
    print(copyA)
    print(copyB)
    
    # sums them together
    for i in range(len(created_list)):
        created_list[i] = copyA[i]+copyB[i]
    
    return created_list


# # Define a function named insert_word_before_target with three parameters,
# # a list of strings, a target word, and an insert word. Create a shallow 
# # copy of the list. Then check to see if the target word exists in the list. 
# # If it does, insert the insert word immediately before the first instance 
# # of the target word in the list. If the target word does not exist in the 
# # list add it to the end of the list. Return the new list.
def insert_word_before_target(string_list:list, target:str,new_word:str)->list:
    """
    >>> word_list = ['apple', 'banana', 'cherry', 'banana', 'date']
    >>> insert_word_before_target(word_list, 'banana', 'strawberry')
    ['apple', 'strawberry', 'banana', 'cherry', 'banana', 'date']
    >>> word_list = ['apple', 'banana', 'cherry', 'banana', 'date']
    >>> insert_word_before_target(word_list, 'blueberry', 'strawberry')
    ['apple', 'banana', 'cherry', 'banana', 'date', 'strawberry']
    >>> insert_word_before_target([], 'blueberry', 'strawberry')
    ['strawberry']
    """
    #create a shallow copy
    a_list: list = string_list[:]

    #check if the target is in the list
    if target in a_list:
        where = a_list.index(target) #where is it
        a_list.insert(where, new_word) #insert my word there
    else:
        a_list.append(new_word)
    return a_list

if __name__ == "__main__":
    doctest.testmod(verbose=True)






