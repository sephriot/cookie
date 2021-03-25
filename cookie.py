from kivy import Config
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.uix.floatlayout import FloatLayout

from shapebutton import ShapeButton
from picture import Picture
from pictureview import PictureView
from listview import ListView


class Cookie(FloatLayout):

    def __init__(self, **kwargs):
        super(Cookie, self).__init__(**kwargs)
        self.ids.picture.bind(last_drawing=self.drawing_callback)
        self.ids.list_view.layout_manager.bind(selected_nodes=self.drawing_selection_callback)
        self.drawings = []
        self.last_selected = -1

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

    def drawing_callback(self, instance, value):
        self.ids.list_view.data.append({'text': self.ids.picture.draw_mode})
        self.ids.list_view.layout_manager.clear_selection()
        self.drawings.append(value)

    def drawing_selection_callback(self, instance, value):
        if len(value) == 0:
            return

        self.paint_object(self.drawings[self.last_selected], Color(1, 1, 0))
        self.last_selected = value[0]
        self.paint_object(self.drawings[self.last_selected], Color(1, 0, 0))

    def paint_object(self, instance, color):
        self.ids.picture.canvas.remove(instance)
        instance.remove(instance.children[0])
        instance.insert(0, color)
        self.ids.picture.canvas.add(instance)
        self.ids.picture.canvas.ask_update()

    def delete_drawing(self):
        if len(self.drawings) == 0:
            return

        self.ids.picture.canvas.remove(self.drawings[self.last_selected])
        del self.drawings[self.last_selected]
        del self.ids.list_view.data[self.last_selected]
        self.last_selected = -1
        self.ids.list_view.layout_manager.clear_selection()


class CookieApp(App):

    def build(self):
        return Cookie()


if __name__ == '__main__':
    Config.read('config.ini')
    CookieApp().run()
