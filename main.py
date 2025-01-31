from kivy.app import App
from kivy.clock import Clock
import os

class WizLightsOffApp(App):
    def build(self):
        Clock.schedule_once(lambda dt: self.turn_off_wiz(), 0.1)
        return None  # No UI needed

    def turn_off_wiz(self):
        os.system("python3 -m pywizlight.cli off --ip 192.168.0.78")
        self.stop()  # Close the app after execution

# Run the app
WizLightsOffApp().run()
