from pad4pi import rpi_gpio
import RPi.GPIO as gp
from time import sleep

gp.setwarnings(False)


keypad = [
    [1,2,3,'A'],
    [4,5,6,'B'],
    [7,8,9,'C'],
    ['*',0,'#','D']
    ]

ROW_PINS = [5,6,13,19]
COL_PINS = [12,16,20,21]

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad = keypad, row_pins = ROW_PINS, col_pins = COL_PINS)
print('Enter the four digit code')

code = ''
maxx = 0
def printKey(key):
    global code
    global maxx

    code += str(key)

    if len(code) == 4:
        if code == 'ABCD':
            print('You have entered the correct code')
            print('*'*25)
            code = ''
        else:
            maxx += 1
            print('Wrong code entered')
            print('*'*25)
            code = ''
            
        
    if len(code) == 0:
        print('Enter four digit code')

    if maxx == 3:
        print('you have entered maximum number of times')
        maxx = 0
        print('try again after 30 sec')
        sleep(3)
        print('Enter four digit code')

keypad.registerKeyPressHandler(printKey)

