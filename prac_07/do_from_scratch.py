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

ConvertMilesToKm().run()