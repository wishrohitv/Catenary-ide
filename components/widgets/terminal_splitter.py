from kivy.graphics import Color, Rectangle
from kivy.uix.splitter import Splitter


class TerminalSplitter(Splitter):
    def __init__(self, **kwargs):
        super(TerminalSplitter, self).__init__(**kwargs)
        self.size_hint = 1, .4
        self.strip_size = '3pt'
        self.sizable_from = "top"
        with self.canvas:
            Color(rgba=(60 / 255, 48 / 255, 72 / 255, 1))
            #Rectangle(pos=self.pos, size=self.size)
