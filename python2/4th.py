"""
4. Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
"""

lists = []

initialId = id(lists)

lists.append('Ram')
lists.append('Shyam')
lists.append('Hari')
lists.append('Sita')
lists.append('Gita')
lists.append('Rita')

finalId = id(lists)

if initialId == finalId:
    print('{} id has not been changed' .format(initialId))

else:
    print('{} id has been changed to {} '.format(initialId , finalId))

lists.sort()

print('first item  is {}' .format(lists[0]))
print('second item  is {}' .format(lists[1]))

print('third item  is {}' .format(lists[2]))
print('fourth item  is {}' .format(lists[3]))

print('fifth item  is {}' .format(lists[4]))
print('sixth item  is {}' .format(lists[5]))



