import doctest
import copy
###################################################
# Coder: Aden Clymer
# Assignment: Problem Set 7
# Date: 31st October 2023
###################################################


# The required parameter is a string representing a file name 
# optional parameter is a Boolean with a default value of True.
# Your function must open the .csv file located at the file path, 
# read its contents,and convert its contents into a two-dimensional 
# nested list of integers. If the Boolean is True, you should remove 
# the first row (the “header”) and the first column (the “id” column). 
# Return the resulting nested list of integers. Your function should
# work with a .csv file of any dimension. Assume the file exists.
def process_csv_file(file_name:str, header: bool = True)->list[list[int]]:
    '''
    >>> file_name = 'tester.csv'
    >>> process_csv_file(file_name)
    [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
    '''
    with open(file_name, "r") as f:
        return_list = []
        if header == True: 
            removed = False
        for line in f:
            line = line.strip()
            row = line.split(",")
            if removed == False:
                removed = True
                continue
            if header == True:
                row.remove(row[0])
            for i in range(len(row)):
                row[i] = int(row[i])
            #print(line) # used to check self
            #print(row) # used to check self
            return_list.append(row)
        return return_list
            


# Define a procedure named update_matrix with 4 parameters: 
    # a list of list
    # integer representing a row
    # integer representing a column
    # integer value. 
# Replace the value at the location specified by the second 
# and third arguments with the fourth argument
def update_matrix(a_list: list, row: int, col:int, value:int):
    '''
    >>> my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> update_matrix(my_matrix, 1, 1, 0)
    >>> my_matrix
    [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    >>> update_matrix(my_matrix, 2, 0, 42)
    >>> my_matrix
    [[1, 2, 3], [4, 0, 6], [42, 8, 9]]
    '''
    a_list[row][col] = value


# Define a function named update_matrix_v2 with 4 parameters: 
#   list of lists,
#   integer representing a row, 
#   integer representing a column, 
#   integer value. 
# Replace the value at the location specified by the second and 
# third arguments with the fourth argument and return the modified 
# list. The original list should remain unchanged. This one 
# requires deeper thought than the last question.
def update_matrix_v2(a_list:list, row:int, col:int, value:int):
    '''
    >>> my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> update_matrix_v2(my_matrix, 1, 1, 99)
    [[1, 2, 3], [4, 99, 6], [7, 8, 9]]
    >>> my_matrix
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    '''
    new_list = copy.deepcopy(a_list)
    new_list[row][col] = value
    return new_list


# Define a class named M16Rifle. Provide two arguments: 
#   A string as the owner's name 
#   A boolean to whether or not the weapon is loaded.
# Each rifle has a serial number. There is a file where name
# is the owner of the rifle and the only contents of the file 
# is the serial number of that individual's rifle. If the weapon is
# loaded then you should keep track of that weapon's ammo as you 
# see fit. A loaded weapon has a full magazine of 30 rounds and 
# an unloaded weapon has 0 rounds in it
def find_serial(name:str)->str:
        with open(name, "r") as f:
            for line in f:
                line = line.strip()
                return line

class M16Rifle(object):
    def __init__(self,owner:str, loaded:bool) -> None:
        '''
        >>> alice_rifle = M16Rifle("Alice", False)
        >>> alice_rifle.owner
        'Alice'
        >>> alice_rifle.serial_number
        '3909611'
        '''
        self.owner = owner
        self.loaded = loaded
        self.serial_number = find_serial(owner+".txt")
        if self.loaded == True:
            self.ammo = 30
        elif self.loaded == False:
            self.ammo = 0
    

    # Define a method for the class M16Rifle called my_human. 
    # This method should display a string in the format 
    # Rifle <serial_number> belongs to <owner>
    def my_human(self)->str:
        '''
        >>> bob_rifle = M16Rifle("Bob", True)
        >>> bob_rifle.my_human()
        Rifle 1510388 belongs to Bob.
        '''
        the_human = "Rifle "+self.serial_number+" belongs to "+self.owner+"."
        print(the_human)

    # We should be able to check if your rifle is empty or not. 
    # Write a method called is_loaded to determine if you still 
    # have at least one round of ammunition left
    def is_loaded(self)->bool:
        '''
        >>> alice_rifle = M16Rifle("Alice", False)
        >>> bob_rifle = M16Rifle("Bob", True)
        >>> bob_rifle.is_loaded()
        True
        >>> alice_rifle.is_loaded()
        False
        '''
        if self.ammo >= 1 and self.loaded == True:
            self.loaded = True
            return True
        else:
            self.loaded = False
            return False


    # Create a method fire that takes an integer of the number 
    # of times you want to shoot at your target. 
    # For every shot your rifle fires, print a `!` so we know 
    # it fired. If it can't fire, print a `?`. When your rifle 
    # is out of ammunition, it should only fail to fire once
    def fire(self, shots:int)->str:
        '''
        >>> bob_rifle = M16Rifle("Bob", True)
        >>> bob_rifle.fire(1)
        !
        >>> bob_rifle.fire(3)
        !!!
        >>> alice_rifle = M16Rifle("Alice", False)
        >>> alice_rifle.fire(1)
        ?
        >>> alice_rifle.fire(3)
        ?
        '''
        if self.loaded == True:
            self.ammo -= shots
            print("!"*shots)
        else:
            print("?")

    # Create a method called reload. It should do what you think it would do.
    def reload(self):
        '''
        >>> alice_rifle = M16Rifle("Alice", False)
        >>> alice_rifle.reload()
        >>> alice_rifle.fire(5)
        !!!!!
        >>> alice_rifle.fire(5)
        !!!!!
        >>> alice_rifle.is_loaded()
        True
        >>> alice_rifle.fire(20)
        !!!!!!!!!!!!!!!!!!!!
        >>> alice_rifle.is_loaded()
        False
        '''
        self.loaded = True
        self.ammo = 30



if __name__ == "__main__":
    doctest.testmod(verbose=True)