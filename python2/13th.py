"""
Write a function to write a comma-separated value (CSV) file. It
should accept a filename and a list of tuples as parameters. The
tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22John,54 Love Ave,21
"""

import csv

lists = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]


def func(lists):

    with open('file13.csv' , 'w' , newline= '') as file1:
        fileWrite = csv.writer(file1)
        details = ['name' , 'address' , 'age']
        fileWrite.writerow(details)

        for detail in lists :
            fileWrite.writerow(list(detail))

    file1.close()

func(lists)