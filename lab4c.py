#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    """
    Takes two lists and returns a dictionary using the keys and values.
    Uses a while loop to iterate through both lists.
    """
    result = {}
    i = 0
    while i < len(keys) and i < len(values):
        result[keys[i]] = values[i]
        i += 1
    return result

def shared_values(dict1, dict2):
    """
    Takes two dictionaries and returns a set of values shared between them.
    """
    values1 = set(dict1.values())
    values2 = set(dict2.values())
    return values1 & values2  # Intersection

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
