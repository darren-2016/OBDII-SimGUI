import serial

print ('OBD-II Sim Gui')

ser = serial.Serial()
ser.baudrate = 38400
ser.port = '/dev/tty.SLAB_USBtoUART'
ser.timeout = 4
ser.open()

print (ser.name)
ser.write(b'ATZ\r')
text = ser.readlines()
print (text)

#text = ser.readline()
#print (text)

#text = ser.readline()
#print (text)
####ser.flush()
ser.close()