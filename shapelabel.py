from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from selectableitem import SelectableItem


class ShapeLabel(BoxLayout, SelectableItem):
    type = StringProperty()
    length = NumericProperty()
    area = NumericProperty()
    volume = NumericProperty()
