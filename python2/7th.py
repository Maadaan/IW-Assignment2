"""
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
"""

friends = ([('Ram','Bahadur', 40), ('Shyam','Bahadur',22) , ('Hari','Bahadur',10 , ('Gopal','Bahadur',30) ,('Sita','Kumari' , None)])

agesOfFriends = [x[2] for x in friends]
sumOfAges = 0
ageCount = 0

for age in agesOfFriends:
    if age is not None:
        ageCount = ageCount + 1
        sumOfAges = sumOfAges + 1

averageAge = sumOfAges / ageCount

for firstName , lastName , age in friends:
    # print("{} {} age is ' ' " .format(firstName , lastName))
    print(f'{firstname} {lastname}', end = ' ')
    
    if age is not None :
        if age < averageAge:
            print('young')

        else:
            print('old')
    
    else:
        print('age is unknown !!!')

