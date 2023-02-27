from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.clipboard import Clipboard
import os
from bottom_menu_button import BottomMenuButton
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '420')
Config.set('graphics', 'height', '721')
Config.set('graphics', 'fullscreen', '0')

class Skaner(FloatLayout):
    def copy_button_click(self,button):
        def copy_to_clipboard(widget):
            text = widget.text
            Clipboard.copy(text)
        copy_to_clipboard(self.ids.file_label)
    def reload_button_click(self, button):
        def read_text_and_display(filename, widget):
            with open(filename, "r") as f:
                text = f.read()
            widget.text = text

            def update_widget(dt):
                with open(filename, "r") as f:
                    new_text = f.read()
                widget.text = new_text

            Clock.schedule_interval(update_widget, 1)

        read_text_and_display("text.txt", self.ids.file_label)
    def camera_button_click(self, instance):
        os.system('camera_screen.py')
    def deactivate_buttons(self):
        for key in self.ids:
            if isinstance(self.ids[key],BottomMenuButton):
                self.ids[key].selected= False

class SkanerApp(App):

    def build(self):
        return Skaner()

if __name__ == '__main__':
    SkanerApp().run()
