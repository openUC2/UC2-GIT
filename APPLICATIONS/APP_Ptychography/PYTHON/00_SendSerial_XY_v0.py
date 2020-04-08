import serial

# https://blog.miguelgrinberg.com/post/fun-with-the-arduino-esplora-a-digital-picture-frame 


#serial = serial.Serial("/dev/ttyUSB0",9600)
serial = serial.Serial("/dev/cu.wchusbeserial14640", 9600)

serial.flushInput()

#serial = Serial('/dev/ttyACM0') # <--- enter your own serial port here

# send image data over serial port
serial.write('x')
serial.write('10')
#serial.write('\x00\x00')

serial.write('X')
serial.write('10')
