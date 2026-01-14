def spell_out_time(int: hours)->int:
    '''
    >>> print(spell_out_time(291))
    12 days and 3 hours.
    >>> print(spell_out_time(5))
    0 days and 5 hours
    '''
    days = hours // 24
    new_hours = hours % 24
    time = print(days,"days and", new_hours, "hours.")
    return time
    
 
 
