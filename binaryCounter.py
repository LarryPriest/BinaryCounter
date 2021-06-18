'''binaryCounter.py
June 14, 2021
My binary counter. Displays binary count-up on a string of 8 LED's.
Hardware:
    RaspberryPi Pico
    breadboard or proto/perf board
    8 220 ohm resistors, 8 5mm red LED's
pin 1/GP0 is the High bit in my wiring.
'''


import board
import digitalio
import time

lowByteLed = []

lowByteLed.append(digitalio.DigitalInOut(board.GP0))
lowByteLed[0].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP1))
lowByteLed[1].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP2))
lowByteLed[2].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP3))
lowByteLed[3].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP4))
lowByteLed[4].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP5))
lowByteLed[5].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP6))
lowByteLed[6].direction = digitalio.Direction.OUTPUT
lowByteLed.append(digitalio.DigitalInOut(board.GP7))
lowByteLed[7].direction = digitalio.Direction.OUTPUT

for i in range(256):
    byte = bin(i)[2:]  # leading zeros missing
#     byte = format(i, '08b') # gives full 8 bits
    print(byte)  # reality check
    byte_list = []
    for bit in iter(byte):
        byte_list.append(bit)
    list.reverse(byte_list)  #gits the list to the right
    bit_count = 7  # reverse if u wired the other way up
    for i in iter(byte_list):
        if i == '1':
            lowByteLed[bit_count].value = True
        else:
            lowByteLed[bit_count].value = False
        bit_count -= 1
    time.sleep(0.25)
   
for i in range(len(lowByteLed)):
    lowByteLed[i].deinit()
        