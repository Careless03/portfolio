import doctest

########################################################
# Coder: Aden Clymer
# Problem Set 8, AY24-1
# Date: 20 November 2023
########################################################


# Define a function named most_ufo_sightings with 1 parameter, 
# a dictionary containing the number of recorded UFO sightings 
# per state. (key = US State Code: value = UFO sightings). 
# The function should determine and return the
# highest number of UFO sightings as an integer
def most_ufo_sightings(numbers:dict)->int:
    '''
    >>> ufo_sightings = {'SD':10} 
    >>> most_ufo_sightings(ufo_sightings)
    10
    >>> ufo_sightings = {'NH':14, 'NM':98, 'SD':10}
    >>> most_ufo_sightings(ufo_sightings)
    98
    '''
    value = list(numbers.values())
    maximum = max(value)
    return maximum

        


# Define a function named state_with_most_ufo_sightings 
# with 1 parameter, a dictionary containing the number 
# of recorded UFO sightings per state. 
# (key = US State Code: value = UFO sightings). 
# Return the list, sorted alphabetically, of
# state or in the case of a tie states with the highest 
# number of UFO sightings
def state_with_most_ufo_sightings(state:dict)->list:
    '''
    >>> ufo_sightings = {'SD':10} 
    >>> state_with_most_ufo_sightings(ufo_sightings)
    ['SD']
    >>> ufo_sightings = {'NH':14, 'NM':98, 'SD':10}
    >>> state_with_most_ufo_sightings(ufo_sightings)
    ['NM']
    >>> ufo_sightings = {'NH':14, 'NM':98, 'SD':10, 'CA':98}
    >>> state_with_most_ufo_sightings(ufo_sightings)
    ['CA', 'NM']
    '''
    value = list(state.values())
    maximum = max(value) 
    return_value: list = []   
    for key, value in state.items():
        if value == maximum:
            return_value.append(key)
    return_value.sort()
    return return_value


# Define a function named get_order_total with 2 parameters, 
# The first is a dictionary of item-cost pairs 
# the second is a dictionary of item-quantity pairs. 
# Your function should calculate and return the
# total cost of items in the order, rounded to two decimal places. 
# You can assume that all items in the order have valid prices in 
# the item-cost dictionary.
def get_order_total(item_cost:dict,item_quant:dict)->float:
    '''
    >>> item_costs = {"apple": 0.5,"banana": 0.25,"orange": 0.75}
    >>> item_quantities = {"apple": 3,"banana": 3,"orange": 4}
    >>> total_cost = get_order_total(item_costs, item_quantities)
    >>> print(f"Total cost of the order: ${total_cost}")
    Total cost of the order: $5.25
    >>> item_costs = {"apple": 0.5,"banana": 0.25,"orange": 0.75}
    >>> item_quantities = {"apple": 3,"orange": 5}
    >>> total_cost = get_order_total(item_costs, item_quantities)
    >>> print(f"Total cost of the order: ${total_cost}")
    Total cost of the order: $5.25
    '''
    price: float = 0
    for itemq, quant in item_quant.items():
        for itemc, cost in item_cost.items():
            if itemq == itemc:
                price += float(quant) * float(cost)
    return price


# Define a function named create_team_dict with 1 parameter
# a string representing the name of a file. 
# Assume the file exists and contains NHL statistics
# The function should process the file, 
# consider each player’s team and goals, and 
# return a dictionary that maps team names to the
# total number of goals scored by all players on that team
def create_team_dict(file_name:str)->dict:
    '''
    >>> file_name = 'NHL_2018_test.csv'
    >>> team_dict = create_team_dict(file_name)
    >>> team_dict['PHI']
    23
    >>> sorted(team_dict.items())
    [('CGY', 24), ('COL', 29), ('NYI', 37), ('PHI', 23), ('WSH', 27)]
    '''
    team_dict: dict = {}
    with open(file_name, "r") as f:
        for line in f:
            line = line.strip().split(",")
            if line[0] == "Rk":
                continue
            team = line[4]
            goals = int(line[6])
            if team in team_dict:
                team_dict[team] += int(goals)
                continue
            team_dict[team] = goals
    return team_dict



# Define a function named update_inventory with 2 parameters, 
# a dictionary
# a list of strings. 
# The dictionary contains item-quantity pairs, and the list of
# strings contains item names. The function should modify the 
# item-quantity pair dictionary by removing the item-quantity 
# pairs for the items listed in the list of items. 
# 
# The function should return a list of tuples, each tuple 
# containing an item name and its corresponding quantity, 
# for the item-quantity pairs that were removed from the dictionary. 
# The list should be sorted in alphabetical order of
# the item names. 
# If an item is not in the dictionary the function cannot remove it
# or add the tuple instead it should display the following message: <item> not in
# inventory. eg -> Chisel not in inventory
def update_inventory(inventory:dict, removal:list)->tuple:
    '''
    >>> inventory = {"Widget": 50,"Gadget": 30,"Doodad": 25,"Thingamajig": 10,"Whatchamacallit": 15}
    >>> items_to_remove = ["Widget", "Doohickey", "Doodad", "Thingamajig"]
    >>> update_inventory(inventory, items_to_remove)
    Doohickey not in inventory.
    [('Doodad', 25), ('Thingamajig', 10), ('Widget', 50)]
    >>> inventory
    {'Gadget': 30, 'Whatchamacallit': 15}
    '''
    removal.sort()
    removed:list  = []
    for item in removal:
        if item not in inventory:
            print(f"{item} not in inventory.")
            continue
        for k, v in inventory.items():
            if item == k:
                removed.append((k, v))
        inventory.pop(item)
    return removed

        

if __name__ == "__main__":
    doctest.testmod(verbose=True)
