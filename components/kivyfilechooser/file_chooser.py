from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.app import App

Builder.load_string("""
<FileContent>:
    orientation: "vertical"
    BoxLayout:
        FileChooserIconView:
    BoxLayout:
        size_hint: (1, None)
        height: "40dp"
        Button:
            text: "Close"
        Button:
            text: "Ok"
            



""")


class CFileChooser(Popup):
    pass

class FileContent(BoxLayout):
    pass

class M(App):
    def build(self):
        return FileContent()
M().run()