from kivy.properties import BooleanProperty
from kivy.uix.button import Button


class ShapeButton(Button):
    selected = BooleanProperty(False)