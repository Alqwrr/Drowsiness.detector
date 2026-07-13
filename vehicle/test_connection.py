from esp32 import ESP32Controller
from commands import *


esp = ESP32Controller()


esp.send_command(FORWARD)

esp.send_command(STOP)

esp.close()