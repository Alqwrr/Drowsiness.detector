import socket


class VehicleController:
    def __init__(self,
                 host="192.168.4.1",
                 port=5000):

        self.host = host
        self.port = port

        self.socket = None
        self.last_command = None

    def connect(self):
        try:
            self.socket = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            self.socket.settimeout(5)

            self.socket.connect(
                (self.host, self.port)
            )

            self.last_command = None

            print("Connected to ESP32")

            return True

        except Exception as e:

            print("Connection failed:", e)

            self.socket = None

            return False

    def send(self, command):

        if command == self.last_command:
            return

        print("sending command: ", command)

        try:

            self.socket.sendall(
                (command + "\n").encode()
            )

            self.last_command = command

        except Exception as e:

            print(e)

            self.socket = None

    def disconnect(self):

        if self.socket:

            self.socket.close()

            self.socket = None

            print("Disconnected")