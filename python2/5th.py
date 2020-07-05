"""
5. Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
"""

personalData = ('Ram','Bahadur', 23)

people = [personalData]

friend1 = ('Shyam','Bahadur',22)
friend2 = ('Hari','Bahadur',23)
friend3 = ('Gopal','Bahadur',24)

people.append(friend1)
people.append(friend2)
people.append(friend3)

people.sort()

people.sort(key=lambda detail: detail[0])
print(people)