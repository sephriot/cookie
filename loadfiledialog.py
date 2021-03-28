from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class LoadFileDialog(BoxLayout):

    load = ObjectProperty()
    cancel = ObjectProperty()

    def __init__(self, **kwargs):
        super(LoadFileDialog, self).__init__(**kwargs)
        pass
