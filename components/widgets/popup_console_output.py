from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView

Builder.load_string("""
<ConsoleOutPutPopup>:
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: root.log_text
            size: self.texture_size
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]
""")


class ConsoleOutPutPopup(ScrollView):
    log_text = StringProperty()

    def __init__(self, log, **kwargs):
        super().__init__(**kwargs)
        self.log_text = log
