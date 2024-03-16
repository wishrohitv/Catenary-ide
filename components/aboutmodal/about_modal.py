from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty

Builder.load_string("""    
<AboutModal>:
    BoxLayout:
        id: box
        orientation: root.orient
        size_hint: .8,.8
        Label:
            text: "hello"
        Button:
            text: "ds"

""")

class AboutModal(ModalView):
    orient = StringProperty("horizontal")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.8, .7)
        self.background_color = "purple"
    
    def on_size(self, instance, value):
        x, y = value

        if x < 600:
            self.orient = "vertical"
            
        else:
            self.orient = "horizontal"

    def about_open(self):
        self.open()