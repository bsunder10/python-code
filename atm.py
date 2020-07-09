import time
import serial
import random

data = serial.Serial(port = '/dev/ttyS0',
                     baudrate = 9600,
                     )

names = {b'2B006CCA94':'Bob',b'2B006D2C42':'Alex'}
AccBal = {'Bob':133.0,'Alex':128.0}
AccNo = {'1234':'Bob','2345':'Alex'}
pin = {b'2B006CCA94':1357,b'2B006D2C42':2468}


def banking(a):
    c = input('1 for Transfer\n2 for Account Balance\n')
    if(c == '1'):
        ac = input('Enter the Account Number:')
        acc = input('Conform the Account Number:')
        if(acc == ac):
            if ac in AccNo.keys():
                nam = AccNo.get(ac)
                print('Sending to',nam)
                am = input('Enter the Amount')
                if(AccBal.get(a) > float(am)):
                    tp = random.randrange(100000,999999)
                    print(tp)
                    ot = input('Enter the OTP')
                    if(int(ot) == tp):
                        print('Transfering the amount')
                        a = float(AccBal.get(a))
                        b = float(am)
                        a = a - b
                        AccBal[a] = a
                else:
                    print('Not Enough balance')
            else:
                print('no account is found')
        else:
            print('Account Number did not match')
    elif(c == '2'):
        print(AccBal.get(a))


def withdraw(a):
    amo = input('Enter the amount to withdraw:')
    if(AccBal.get(a) > float(amo)):
        print('Withdrawing',amo)
        wet = input('Do you want to display balance amount ')
        a = AccBal.get(a)
        b = float(amo)
        a = a-b
        AccBal[a] = a        
        if(wet == 'yes'):
            print(AccBal.get(a))
        
    else:
        print('Not enough amount present')


def deposit(a):
    amo = input('Enter the amount to deposit:')
    print('depositing',amo)
    a = float(AccBal.get(a))
    b = float(amo)
    a = a+b
    AccBal[a] = a

    wet = input('Do you want to display balance amount  ')
    if(wet == 'yes'):
        print(AccBal.get(a))
   

while True:
    print('place the card')
    d = data.read(10)
    if(d in names.keys()):
        m = names.get(d)
        print('Welcome Mr',m)
        p = input('Enter the pin:')
        if(int(p) == pin.get(d)):
            c = input('1 for Banking \n2 for Withdrawal \n3 for Deposit\n')
            if(c == '1'):
                banking(names.get(d))
            elif(c == '2'):
                withdraw(names.get(d))
            elif(c == '3'):
                deposit(names.get(d))
                
                


