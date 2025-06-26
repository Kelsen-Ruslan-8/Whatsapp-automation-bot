import csv
import logging
from send_message import send_message

#logging 
logging.basicConfig(filename='send_log.txt',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )
logging.info('Test message logged')

# read contacts and send message 
with open('contacts.csv', mode='r') as file:
    reader = csv.reader(file)
    #next(reader)

    for row in reader:
        name = row[0]
        phone = row[1]
        message = row[2]
        hour = int(row[3])
        minute = int(row[4])
        try:
            print(f'Sending message to {name} at {hour}:{minute}...')

            send_message(phone, message, hour, minute)

            logging.info(f'sent to {name} ({phone}): "{message}" at {hour}: {minute} ')

        except Exception as e:

            print(f'failed to send to {name}: {e}')
            logging.error(f'Failed to send to {name} ({phone}): {e}')
      
