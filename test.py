import csv

with open('contact.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    row = next(reader)

    
    print('Testing contact')
    print('Name:', row[0])
    print('Phone:', row[1])
    print('Message:', row[2])
    print('Hour:', row[3])
    print('minutes', row[4])