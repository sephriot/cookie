from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.button import Button


class ShapeButton(Button):
    selected = BooleanProperty(False)
    name = StringProperty()