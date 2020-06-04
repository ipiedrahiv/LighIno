# LighIno
A python + arduino cooperation to turn on a led if you have an unread e-mail.

Full documentation in spanish: https://docs.google.com/document/d/1R2HHz5S_LBcSu7UDs2e7u6V8PTjAYHCdYkvF-RukOk8/edit?usp=sharing

## Python Script
An IMAP based script that fetches the amount of unread mails in your inbox, and according to it comunicates through the 
serial port with the Arduino of your choice (at the oment the COM port is burnt in the ArduinoYunSerial variable). 

This app has exclusively educational purposes, and therefore the security standards are not the highest, you'll need to 
turn down gmail security settings in order to use this.

To run the script, run on you bash or shell the following command
python unseen_funcions.py <e-mail adress> <e-mail password> 

## Arduino Program
The arduino counterpart will send a starter message by serial to python in order to begin comunication, adter this it will read
the serial input given by python and turn an LED on or of respectively.

It is fundamental that the arduino code is loaded to the device before running the python script, otherwise they will
block each other in the communication port.
