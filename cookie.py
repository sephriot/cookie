from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

import shapebutton

class Cookie(FloatLayout):

    def deactivate_buttons(self):
        self.ids.line_button.selected = False
        self.ids.circle_button.selected = False
        self.ids.rectangle_button.selected = False
        self.ids.freeform_button.selected = False

    def line_button_click(self):
        next_state = not self.ids.line_button.selected
        self.deactivate_buttons()
        self.ids.line_button.selected = next_state
        print("Line")

    def circle_button_click(self):
        next_state = not self.ids.circle_button.selected
        self.deactivate_buttons()
        self.ids.circle_button.selected = next_state
        print("Circle")

    def rectangle_button_click(self):
        next_state = not self.ids.rectangle_button.selected
        self.deactivate_buttons()
        self.ids.rectangle_button.selected = next_state
        print("rectangle")

    def freeform_button_click(self):
        next_state = not self.ids.freeform_button.selected
        self.deactivate_buttons()
        self.ids.freeform_button.selected = next_state
        print("freeform")


class CookieApp(App):

    def build(self):
        return Cookie()


if __name__ == '__main__':
    CookieApp().run()
