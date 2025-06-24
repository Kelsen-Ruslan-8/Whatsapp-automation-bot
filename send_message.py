import csv
import pywhatkit
with open('contacts.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)

    row = next(reader)
    name = row[0]
    phone = row[1]
    message = row[2]
    hour = int(row[3])
    minute = int(row[4])

    print(f'Sending message to {name} at {hour}:{minute}...')

    pywhatkit.sendwhatmsg(phone, message, hour, minute)
    


