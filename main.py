# libraries
import time
import serial
from send_email import sending_email
from obj_detect import detecting_object
global arduino
arduino = serial.Serial('COM3', 9600)



# while loop for detecting objects and then putting the trash into the right bin (it will keep doing this)
while True:
    i = detecting_object()
    print(i)
    # converts the string to a 8-bit value
    msg = arduino.write(i.encode())
    print(msg)
    time.sleep(5)

    # the arduino sends bytes back to python so we need to decode it
    data_packet = arduino.readline().decode("ascii")
    print(data_packet)

    # while a message has not been given whether either bin is full or not, it will execute the code below and keep checking for any message that arduino might send
    while "r full" not in data_packet or "g full" not in data_packet or "not full" not in data_packet:
        print("waiting")
        data_packet = arduino.readline().decode('ascii')
        print(data_packet)

        # once a message has been sent it can include either of these strings. It wille xecute the code based on the string that was sent
        if data_packet == "r full":
            # sending email
            print("closing opening and sending email")
            sending_email('recycling')

        elif data_packet == "g full":
            # sending email
            print("closing opening and sending email")
            sending_email('garbage')

        elif data_packet == "not full":
            print("not full")
