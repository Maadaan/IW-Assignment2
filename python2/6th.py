"""
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""

names = ['Ram', 'Shyam' , 'Hari' , 'Gopal', 'John' , 'Sita' , 'Gita' , 'Rita']

for name in names:
    if name == 'John':
        print('John Found !!!')
        break
else:
    print('John Not Found !!!')