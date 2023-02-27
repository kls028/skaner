from kivy.uix.button import Button
from kivy.properties import BooleanProperty, StringProperty
class BottomMenuButton(Button):
    selected = BooleanProperty(False)
    name= StringProperty()