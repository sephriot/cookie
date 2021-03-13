from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from shapebutton import ShapeButton
from picture import Picture
from pictureview import PictureView


class Cookie(FloatLayout):

    def shape_button_click(self, button):
        next_state = not button.selected
        self.deactivate_buttons()
        button.selected = next_state
        print(button.name)

    def deactivate_buttons(self):
        for key in self.ids:
            if isinstance(self.ids[key], ShapeButton):
                self.ids[key].selected = False


class CookieApp(App):

    def build(self):
        return Cookie()


if __name__ == '__main__':
    CookieApp().run()
