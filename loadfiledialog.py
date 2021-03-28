import os
import string

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from listview import ListView


class LoadFileDialog(BoxLayout):
    load = ObjectProperty()
    cancel = ObjectProperty()

    def __init__(self, **kwargs):
        super(LoadFileDialog, self).__init__(**kwargs)
        self.ids.drives_list.layout_manager.bind(selected_nodes=self.drive_changed)
        self.ids.drives_list.data = [{'text': '/'}]
        for s in string.ascii_uppercase:
            if os.path.exists(s + ':'):
                self.ids.drives_list.data.append({'text': s + ':'})

    def drive_changed(self, instance, value):
        if len(value) > 0:
            self.ids.filechooser.path = self.ids.drives_list.data[value[0]]['text']
