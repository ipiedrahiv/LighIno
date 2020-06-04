import imaplib
import email
import sys
import serial
import time
from gpiozero import LED

ArduinoYunSerial = serial.Serial('/dev/tty.usbmodem14201',9600)   

def main():
    print(ArduinoYunSerial.readline())
    while(True):
        new_mails = get_new_mails(sys.argv[1], sys.argv[2])
        num_new_mails = count_mails(new_mails)

        if (notify(num_new_mails)):
            print('1')
            ArduinoYunSerial.write(b'1')
            time.sleep(1)
        else:
            ArduinoYunSerial.write(b'0')
            print('0')
            time.sleep(1)

        print(ArduinoYunSerial.readline())
       
    return notify(num_new_mails)

    
def get_new_mails(user, password):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')	
        mail.login(user, password)
        mail.select() # connect to inbox.
        data = mail.search(None, ('UNSEEN'))
        #count = len(mail_ids[0].split(" "))
    	      
    except Exception as e: print(e)

    return (data)


def count_mails(data):
    num = len(data[1][0].decode("utf-8").split(" "))
    if (data[1][0].decode("utf-8").split(" ") == ['']):
        return 0
    else:
        return num
    
def notify(num_new_mails):
    return (num_new_mails >= 1)

print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

main()
