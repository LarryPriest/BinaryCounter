'''binaryCounter.py
June 14, 2021
Author: Larry Priest email: larrytpriest@gmail.com
My binary counter. Displays binary count-up on a string of n LED's.
Hardware:
    RaspberryPi Pico
    breadboard or proto/perf board
    n 220 ohm resistors, n 5mm red LED's
pin 1/GP0 is the High bit in my wiring.
'''


import board
import digitalio
import time

bits = 15  # start at zero
delay = 0.25  # seconds
count = 0xffff  # any interger (hex 'cause it makes sense)
lowByteLed = []

# Setup LED list
subcommand = 'lowByteLed.append(digitalio.DigitalInOut(board.GP'
for i in range(bits+1):
    fullcommand = subcommand + str(i) + '))'
    exec(fullcommand)
    lowByteLed[i].direction = digitalio.Direction.OUTPUT

# main loop
for i in range(count):
    byte = bin(i)[2:]  # leading zeros missing
#     byte = format(i, '08b') # gives full 8 bits
    print(byte)  # reality check
    byte_list = []
    for bit in iter(byte):
        byte_list.append(bit)
    list.reverse(byte_list)  # gits the list to the right
    bit_count = bits  # reverse if u wired the other way up
    for i in iter(byte_list):
        if i == '1':
            lowByteLed[bit_count].value = True
        else:
            lowByteLed[bit_count].value = False
        bit_count -= 1
    time.sleep(delay)

for i in range(len(lowByteLed)):
    lowByteLed[i].deinit()
