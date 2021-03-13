from kivy.properties import StringProperty
from kivy.uix.scatter import Scatter


class Picture(Scatter):
    source = StringProperty()

    def on_touch_down(self, touch):
        if touch.button == "scrolldown":
            self.scale *= 1.25
        elif touch.button == "scrollup":
            self.scale *= 0.8
        return super(Picture, self).on_touch_down(touch)