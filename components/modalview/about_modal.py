from kivy.uix.modalview import ModalView
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string("""    
<AboutModal>:
    BoxLayout:
        size_hint: .8,.8
        Label:
            text: "hello"
        Button:
            text: "ds"

""")

class AboutModal(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.8, .7)
        self.background_color = "purple"

    def about_open(self):
        self.open()