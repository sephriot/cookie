from kivy.uix.recycleview import RecycleView

from selectablelabel import SelectableLabel
from listviewlayout import ListViewLayout


class ListView(RecycleView):

    def __init__(self, **kwargs):
        super(ListView, self).__init__(**kwargs)
