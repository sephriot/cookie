from kivy.uix.scrollview import ScrollView


class PictureView(ScrollView):

    def on_touch_down(self, touch):
        if touch.button == "scrolldown" or touch.button == "scrollup":
            for child in self.children:
                child.on_touch_down(touch)
        super(PictureView, self).on_touch_down(touch)