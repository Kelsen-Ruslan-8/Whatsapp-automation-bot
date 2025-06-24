import csv
with open('contacts.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    while True:
        contact ={
            'name': input('Name:'),
            'Phone_number': input('Phone_number:'),
            'Message': input('Message:'),
            'time_hours':input('Hours:'),
            'time_minutes': input('minutes:')
            }
        
        print(f'\nSaving contac:{contact}')

        writer.writerow(contact.values())

        again = input('Add another contact? (yes/no):')
        if again.lower() != 'yes':
            break