from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from shapebutton import ShapeButton
from picture import Picture
from pictureview import PictureView


class Cookie(FloatLayout):

    def enable_draw_mode(self, mode):
        self.ids.picture.draw_mode = mode
        self.ids.picture_view.scroll_timeout = 1
        self.ids.picture_view.scroll_distance = 100000

    def disable_draw_mode(self):
        self.ids.picture_view.scroll_timeout = 200
        self.ids.picture_view.scroll_distance = 20
        self.ids.picture.draw_mode = ""

    def shape_button_click(self, button):
        next_state = not button.selected
        self.deactivate_buttons()
        button.selected = next_state
        print(button.name)
        if next_state:
            self.enable_draw_mode(button.name)

    def deactivate_buttons(self):
        self.disable_draw_mode()
        for key in self.ids:
            if isinstance(self.ids[key], ShapeButton):
                self.ids[key].selected = False


class CookieApp(App):

    def build(self):
        return Cookie()


if __name__ == '__main__':
    CookieApp().run()
