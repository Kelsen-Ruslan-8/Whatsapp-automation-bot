import csv
import pywhatkit
import pyautogui
import time



with open('contacts.csv', mode='r') as file:
    reader = csv.reader(file)
    #next(reader)

    for row in reader:
        name = row[0]
        phone = row[1]
        message = row[2]
        hour = int(row[3])
        minute = int(row[4])

        print(f'Sending message to {name} at {hour}:{minute}...')
        try:
            pywhatkit.sendwhatmsg(phone, message, hour, minute)
            time.sleep(15)
            pyautogui.click()
            pyautogui.press('enter')
            print(f'message to {name}scheduled.\n')
        except Exception as e:
            print(f'failed to send message to {name}. Error: {e}')
        time.sleep(15)





