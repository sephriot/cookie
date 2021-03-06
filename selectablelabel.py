from kivy.properties import BooleanProperty
from kivy.uix.label import Label
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from selectableitem import SelectableItem


class SelectableLabel(Label, SelectableItem):
    selected = BooleanProperty(False)
    index = None

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
