while True:
    name = input('Name:')
    phone_num = input('Phone_number:')
    Message = input('What_message_to_send:')
    hours_time = input('What_hours_to_send:')
    minutes_time = input('What_minutes_to_send:')

    again = input('Add another contact? (yes/no):')
    if again.lower() != 'yes':
        break


print('Saving', ',' , name, ',' , phone_num, '"', Message,'"', ',', hours_time,',', minutes_time  )

import csv 

with open('contact.csv', mode='a',newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, phone_num, Message, hours_time, minutes_time])