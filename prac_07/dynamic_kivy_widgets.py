"""
CP1404 Dynamic Kivy Widgets prac exercise
Sean Spring
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

NAMES = ["Sean", "Liam", "Nicholas", "Spring"]

class DynamicKivyWidgets(App):
    """DynamicKivyWidgets is a kivy app designed to test how dynamic widgets work"""

    def build(self):
        """Build GUI"""
        self.title = "Dynamic Kivy Widgets"
        self.root = Builder.load_file('dynamic_kivy_widgets.kv')
        return self.root

DynamicKivyWidgets().run()