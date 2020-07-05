"""
Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
"""



items  = [i for i in range(0,30)]
items.sort()

itemToSearch = 14

itemToSearch = 50

def func(sequence , item):

    try :
        a = sequence.index(item)
    
    except ValueError:
        return -1
    
    return a

print(func(items , itemToSearch))