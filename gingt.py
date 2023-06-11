import serial
import time
import threading

class gingt:

    def __init__(self):
        # Change /dev/ttyUSB0 by COMx in Windows.
        self.serialPort = serial.Serial(port="/dev/ttyUSB0", baudrate=250000, timeout=1)
        time.sleep(5)
        self.readthread = threading.Thread(target=self.Read)
        self.readthread.start()
        self.readOK = False

    def ComClose(self):
        self.serialPort.close()
        return

    def Read(self):

        while True:
            try:
                inmsg = self.serialPort.readline()
                inmsg = inmsg[:-1]
                if len(inmsg) == 0:
                    self.readOK = True
                else:
                    self.readOK = False

                    print(inmsg.decode("utf-8"))

            except Exception as ex:
                self.readOK = True
                pass
            time.sleep(0.001)

    def Write(self, msg):

        # Sends command to the printer
        self.serialPort.write(data=msg.encode())

        # Waits a bit until all data has been transfered
        time.sleep(0.1)

        # Reads response from printer
        #self.Read()
        return

    def Send(self, command):
        pass

def CommandPrompt(term):

    while True:
        command = input(">>")
        term.Write(command + "\n")


if __name__ == "__main__":

    gingt = gingt()
    CommandPrompt(gingt)
    #gcodeTerm.Write("M115")
    #gcodeTerm.ComClose()
