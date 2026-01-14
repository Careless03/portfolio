import math

monthly_payment(float: cost, float: APR)->float:
    '''
    >>> print(monthly_payment(175000, 0.0701))
    1036.26
    >>> print(monethly_payment(225000, 0.0698))
    1361.12
    '''
    
    P = cost - 20000
    numerator = (APR/12) * P
    denominator = 1 - ((1+(APR/12))**-360)
    monthly_pay = numerator/denominator
    rounded_month_pay = round(monthly_pay, 2)
    return rounded_month_pay