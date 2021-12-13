from machine import UART, Pin
from time import sleep

tx = Pin(0, Pin.OUT)
rx = Pin(1, Pin.IN)
en = Pin(2, Pin.OUT)

led = Pin(25, Pin.OUT)
led.high()

sleep(0.5)
led.low()

inputString = ''

uart = UART(0, 9600, tx=tx, rx=rx)
# print('test')
# print(dir(uart))

while True:
    if uart.any():
        print(uart.any())
        while uart.any():
            inputString = uart.read().decode()
            print(type(inputString))
            print(inputString)
            print(inputString.find('a') == 0)

        while uart.any() > 0:
            junk = uart.read()
            print('junk')
            print(junk)

        if inputString.find('a') == 0:
            led.low()
            uart.write(bytes('led Off\n', 'utf-8'))
        elif inputString.find('b') == 0:
            led.high()
            uart.write(bytes('led On\n', 'utf-8'))

