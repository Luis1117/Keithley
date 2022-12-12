import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 2, parity=serial.PARITY_NONE, bytesize=8, stopbits=1,
xonxoff=0 )  # Open serial port

ser.write(':SEN:FUN:')


