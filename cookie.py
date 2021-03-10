from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class Cookie(FloatLayout):
    pass


class CookieApp(App):

    def build(self):
        return Cookie()


if __name__ == '__main__':
    CookieApp().run()
