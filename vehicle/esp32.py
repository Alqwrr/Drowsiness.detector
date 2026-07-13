import serial
import time


class ESP32Controller:


    def __init__(
        self,
        port="COM3",
        baudrate=115200
    ):

        self.connected = False


        try:

            self.serial = serial.Serial(
                port,
                baudrate,
                timeout=1
            )


            time.sleep(2)


            self.connected = True


            print(
                "ESP32 Connected"
            )


        except Exception as e:


            print(
                "ESP32 not connected:",
                e
            )



    def send_command(
        self,
        command
    ):


        if self.connected:


            message = command + "\n"


            self.serial.write(
                message.encode()
            )


            print(
                "Sent:",
                command
            )



    def close(self):

        if self.connected:

            self.serial.close()