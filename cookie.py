from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Cookie(FloatLayout):

    def line_button_click(self):
        print("Line")

    def circle_button_click(self):
        print("Circle")

    def rectangle_button_click(self):
        print("rectangle")

    def freeform_button_click(self):
        print("freeform")


class CookieApp(App):

    def build(self):
        return Cookie()


if __name__ == '__main__':
    CookieApp().run()
