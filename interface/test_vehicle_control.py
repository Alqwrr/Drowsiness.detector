from controls import VehicleControls


controls = VehicleControls()


controls.start()


print(
    "Vehicle control started"
)


while controls.running:


    print(
        "Current command:",
        controls.get_command()
    )