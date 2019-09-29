"""
CP1404 do from scratch Practical
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesToKm(App):
    """ConvertMilesToKm is a kivy app used to convert miles to kilometres"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('do_from_scratch.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            number = int(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(number + increment)
        except:
            self.root.ids.input_number.text = str(increment)

    def handle_conversion(self):
        try:
            self.root.ids.output.text = str(int(self.root.ids.input_number.text) * 1.60934)
        except:
            self.root.ids.output.text = "0.0"

ConvertMilesToKm().run()