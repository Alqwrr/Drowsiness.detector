from pynput import keyboard


class VehicleControls:


    def __init__(self):

        self.command = "STOP"

        self.running = True



    def on_press(self, key):

        try:

            if key.char == "w":

                self.command = "FORWARD"
                print(self.command)


            elif key.char == "s":

                self.command = "BACKWARD"
                print(self.command)


            elif key.char == "d":

                self.command = "LEFT"
                print(self.command)


            elif key.char == "a":

                self.command = "RIGHT"
                print(self.command)



        except AttributeError:


            if key == keyboard.Key.space:

                self.command = "STOP"
                print(self.command)



            elif key == keyboard.Key.esc:

                self.running = False



    def start(self):

        listener = keyboard.Listener(
            on_press=self.on_press
        )


        listener.start()



    def get_command(self):

        return self.command