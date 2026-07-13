from pynput import keyboard


class VehicleControls:


    def __init__(self):

        self.command = "STOP"

        self.running = True



    def on_press(self, key):

        try:

            if key.char == "w":

                self.command = "FORWARD"


            elif key.char == "s":

                self.command = "BACKWARD"


            elif key.char == "a":

                self.command = "LEFT"


            elif key.char == "d":

                self.command = "RIGHT"



        except AttributeError:


            if key == keyboard.Key.space:

                self.command = "STOP"



            elif key == keyboard.Key.esc:

                self.running = False



    def start(self):

        listener = keyboard.Listener(
            on_press=self.on_press
        )


        listener.start()



    def get_command(self):

        return self.command