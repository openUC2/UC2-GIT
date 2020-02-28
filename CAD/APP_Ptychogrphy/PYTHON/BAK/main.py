''' 
IMPORTANT: Execute as sudo
copyright@Bene
License GPLv3
'''
import serial
import time

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame


serial = serial.Serial("/dev/ttyUSB0",9600)
#serial = serial.Serial("/dev/cu.wchusbeserial14640", 9600)
#time.sleep(8)
print('Start programm')

# Flush anything which is on the pipe..
serial.flushInput()

# move stepper forward/backward in X
serial.write(b'x10')
time.sleep(2)
serial.write(b'X10')
time.sleep(2)

# move stepper forward/backward in Y
serial.write(b'y10')
time.sleep(2)
serial.write(b'Y10')
time.sleep(2)

print('Done')
exit()
