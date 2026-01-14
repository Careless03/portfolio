########################################################
# Coder: Aden clymer
# Problem Set 9
# Date: 3 December 2023
########################################################
import doctest
from eBook import *
import copy
import time

# Define a function named is_weekday with one parameter 
# a floating pointnumber that represents a time in seconds since the epoch. 
# Your function should use time.ctime( seconds ) 
# to determine the local time and determine if the
# time provided represents a weekday. 
# If it is a weekday return True otherwise return False
def is_weekday(unk_time: int) -> bool:
    '''
    >>> is_weekday(57232973)
    True
    >>> is_weekday(8138338)
    False
    >>> is_weekday(63980761)
    True
    '''
    day: bool = True
    time_given:str = str(time.ctime(unk_time))
    if "Sat" in time_given or "Sun" in time_given:
        day = False
    return day


# Define a function called get_5_letter_words that takes 
# a set of strings as its sole parameter. 
# The function is designed to produce and return a new set
# containing only the strings with exactly 5 letters from 
# the original set. Ensure
# that the original set remains unaltered
def get_5_letter_words(all_words: set[str]) -> set[str]:
    '''
    >>> all_words = {'hello', 'world', 'pizza', 'banana', 'go'}
    >>> five_letter_words = get_5_letter_words(all_words)
    >>> five_letter_words == {'hello', 'world', 'pizza'}
    True
    >>> all_words == {'hello', 'world', 'pizza', 'banana', 'go'}
    True
    '''
    new_set: set = set()
    for word in all_words:
        if len(word) == 5:
            new_set.add(word)
    return new_set



# Define a function named remove_duplicates that takes 
# a list of values as its sole parameter. 
# The function should remove duplicate values, sort the list, and
# return the result. 
# It is important to ensure that the original list remains
# unaltered. You can assume that the list contains comparable values.
def remove_duplicates(a_list: list) -> list:
    '''
    >>> remove_duplicates([1, 1, 1, 1])
    [1]
    >>> remove_duplicates([1, 2, 3, 4, 2])
    [1, 2, 3, 4]
    >>> abc_list = ['d', 'c', 'b', 'd', 'a', 'b', 'd', 'b', 'c', 'a', 'b']
    >>> remove_duplicates(abc_list)
    ['a', 'b', 'c', 'd']
    >>> abc_list
    ['d', 'c', 'b', 'd', 'a', 'b', 'd', 'b', 'c', 'a', 'b']
    '''
    dup_list:list = copy.deepcopy(a_list)
    new_list: list = []
    for item in dup_list:
        if item in new_list:
            continue
        else:
            new_list.append(item)
    new_list.sort()
    return new_list





# Create a class called Item. 
# An Item must be provided a name when it is created and optionally 
# provided a category for the Item. If no category is provided, 
# an Item is in the “Misc” category. Users can call the describe
# method that returns '{Item name} is in the category {category}.'
# Add a class attribute to the Item class called _registry. 
# The _registry is a dictionary that holds the name and 
# categories of each item. Whenever an Item is created, 
# the name should be added to the dictionary with the category 
# as the value. If the name of the item already exists in the 
# dictionary, raise a ValueError with the message: 'This item
# already exists.'

class Item(object):
    _registry:dict = {}
    def __init__(self,name:str,category:str = "Misc"):
        """
        >>> new_item = Item('Toothbrush', 'Hygiene')
        >>> duplicate_item = Item('Toothbrush', 'Hygiene')
        Traceback (most recent call last):
        ...
        ValueError: This item already exists.
        """
        if name in self._registry:
            raise ValueError("This item already exists.") 
        self.name = name
        self.category = category
        self._registry[name] = category
        
    def describe(self):
        """
        >>> new_item = Item('Apple', 'Fruit')
        >>> new_item.name == 'Apple'
        True
        >>> new_item.category == 'Fruit'
        True
        >>> new_item.describe()
        'Apple is in the category Fruit.'
        """
        return f"{self.name} is in the category {self.category}."

    @classmethod
    def list_items(cls, filter = None): 
        """
        >>> second_item = Item('Car', 'Transportation')
        >>> Item.list_items()
        Items Summary:
        - Apple (Category: Fruit)
        - Car (Category: Transportation)
        - Toothbrush (Category: Hygiene)
        >>> Item.list_items('Hygiene')
        Items Summary:
        - Toothbrush (Category: Hygiene)
        """
        dictionary = cls._registry
        sorted_list:list = []
        for key in dictionary.keys():
            sorted_list.append(key)
        sorted_list.sort()
        print("Items Summary:")
        if filter == None:
            for item in sorted_list:
                print(f"- {item} (Category: {dictionary[item]})")
        if filter != None:
            for item in sorted_list:
                if str(dictionary[item]) == filter:
                    print(f"- {item} (Category: {dictionary[item]})")


# You are provided with an eBook class in the `eBook.py` file. 
# Import that module into your script. Create an eBookCollection 
# class. An eBookCollection is created using a list of eBooks. 
# The list of eBooks should be stored in the instance attribute 
# collection as a set


class eBookCollection(object):
    '''
    >>> my_faves = eBookCollection([eBook('It', 102), eBook('The Shining', 109), eBook('It', 102)])
    >>> my_faves.collection == {eBook('It', 102), eBook('The Shining', 109)}
    True
    '''
    def __init__(self,book_collection:list[eBook]):
        new_collection = []
        for book in book_collection:
            if book not in new_collection:
                new_collection.append(book)
            elif book in new_collection:
                continue
        self.collection = set(new_collection)
    
    def statement(self):
        return self.collection
    # Write a static method named join that takes two eBookCollections as
    # parameters. The class method should return a new eBookCollection that
    # does not include any duplicate books
    @staticmethod
    def join(collection_1, collection_2):
        '''
        >>> my_faves = eBookCollection([eBook('It', 102), eBook('The Shining', 109), eBook('It', 102)])
        >>> my_faves.collection == {eBook('It', 102), eBook('The Shining', 109)}
        True
        >>> my_enemies = eBookCollection([eBook('Grapes of Wrath', 110), eBook('It', 102)])
        >>> joined = eBookCollection.join(my_faves, my_enemies)
        >>> joined.collection == {eBook('It', 102), eBook('The Shining', 109), eBook('Grapes of Wrath', 110)}
        True
        '''
        return eBookCollection(collection_1.collection.union(collection_2.collection)) #from the terminal help desk

    # Write an instance method called missing_books that compares the
    # current eBookCollection (self) against another eBookCollection and
    # returns the set of books in the other eBookCollection but not in the
    # current eBookCollection
    def missing_books(self, enemy):
        '''
        >>> my_faves = eBookCollection([eBook('It', 102), eBook('The Shining', 109), eBook('It', 102)])
        >>> my_enemies = eBookCollection([eBook('Grapes of Wrath', 110), eBook('It', 102)])
        >>> my_faves.missing_books(my_enemies) == {eBook('Grapes of Wrath', 110)}
        True
        '''
        return enemy.collection.difference(self.collection) # from help(set())
                

    # Write an instance method called same_books that compares the current
    # eBookCollection against another eBookCollection and returns which
    # books the two collections have in common.
    def same_books(self, enemy):
        '''
        >>> my_faves = eBookCollection([eBook('It', 102), eBook('The Shining', 109), eBook('It', 102)])
        >>> my_enemies = eBookCollection([eBook('Grapes of Wrath', 110), eBook('It', 102)])
        >>> my_faves.same_books(my_enemies) == {eBook('It', 102)}
        True
        '''
        return enemy.collection.intersection(self.collection) #from help(set())


if __name__ == '__main__':
    doctest.testmod(verbose = True)
    