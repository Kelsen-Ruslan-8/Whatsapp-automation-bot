import pywhatkit

def send_message(phone, message, hour, minute):
    pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time=20)







