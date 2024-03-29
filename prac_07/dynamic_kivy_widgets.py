"""
CP1404 Dynamic Kivy Widgets prac exercise
Sean Spring
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

NAMES = ["Sean", "Liam", "Nicholas", "Spring"]

class DynamicKivyWidgets(App):
    """DynamicKivyWidgets is a kivy app designed to test how dynamic widgets work"""

    def build(self):
        """Build GUI"""
        self.title = "Dynamic Kivy Widgets"
        self.root = Builder.load_file('dynamic_kivy_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in NAMES:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.test_box.add_widget(temp_button)

    def press_entry(self):
        pass

DynamicKivyWidgets().run()