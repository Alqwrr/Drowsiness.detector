from vehicle_controller import VehicleController
import time

car = VehicleController()

car.connect()

time.sleep(1)

car.send("FORWARD")

time.sleep(2)

car.send("STOP")

time.sleep(1)

car.send("LEFT")

time.sleep(2)

car.send("STOP")

time.sleep(1)

car.send("RIGHT")

time.sleep(2)

car.send("STOP")

time.sleep(1)

car.send("BACKWARD")

time.sleep(2)

car.send("STOP")

car.disconnect()