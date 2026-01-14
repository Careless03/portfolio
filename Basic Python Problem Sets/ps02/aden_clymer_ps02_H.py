####################################
# Coder: Aden Clymer
# Assignment: Problem Set 2
# Date: 9/4/2023
###################################
import doctest
def calculate_conversion(cost, exchange_rate, Euros_USD=True):
	'''
	Given an amount of money, an exchange rate, and an optional boolean value
	(default value = True) calculate and return money conversion. If the boolean
	is True convert from Euros to USD if False convert USD to Euros
	>>> calculate_conversion(10.00, 1.0817)
	10.817
	>>> calculate_conversion(10.00, 1.0817, False)
	9.244707405010631
	'''
	if Euros_USD == True:
		true_cost = cost * exchange_rate

	elif Euros_USD == False:
		true_cost = cost / exchange_rate
	return true_cost
calculate_conversion(10.00, 1.0817)
calculate_conversion(10.00, 1.0817, False)
def is_approval_required(km_away):
	'''
	Given a distance in km determine if a pass is required. If the distance is
	greater than 50 miles return True as a pass is required else return False
	>>> is_approval_required(85)
	True
	>>> is_approval_required(75)
	False
	'''
	miles_away = km_away * 5/8
	if miles_away > 50:
		return True
	elif miles_away <= 50:
		return False
is_approval_required(85)
is_approval_required(75)
def where_to(weekend_length, budget):
	'''
	Given the length of the weekend and a budget return a string representing
	the name of a city to visit.
	>>> where_to(2, 150)
	'Frankfurt'
	>>> where_to(3, 350)
	'Oslo'
	'''
	if weekend_length <= 2:
		if budget > 150:
			return 'Zurich'
		elif budget <= 150:
			return 'Frankfurt'
	elif weekend_length > 2:
		if budget > 300:
			return 'Oslo'
		elif budget <= 300:
			return 'Zagreb'
where_to(2,150)
where_to(3,350)
def most_travelled(A, B, C):
	'''
	>>> most_travelled(10, 5, 10)
	'AC'
	>>> most_travelled(10, 15, 10)
	'B'
	'''
	traveled_most = ""
	if (A >= B) and (A >= C):
		traveled_most += "A"
	if (B >= A) and (B >= C):
		traveled_most += "B"
	if (C >= A) and (C >= B):
		traveled_most += "C"
	return traveled_most

if __name__ == '__main__':
	doctest.testmod(verbose=True)