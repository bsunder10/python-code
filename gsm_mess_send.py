import time
import sys
import serial

phone = serial.Serial("/dev/ttyUSB0", baudrate = 9600, timeout = 1)
message = b'hi'
phone.write(b"AT+CMGF=1\r")
time.sleep(2)
phone.write(b'AT+CMGS = "+919440472852"\r')
time.sleep(2)
phone.write(message+bytes(chr(26),encoding='utf8'))
print('done')




#To Call
'''
phone.write(b'ATD+919440472852;\r')
time.sleep(2)
'''

#To attend call
'''
phone.write(b'ATA\r')
time.sleep(2)
'''

