from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.utils import platform

Builder.load_string("""                                   
<ModalFileChooser>:
    id: file_chooser_popup
    BoxLayout:
        orientation: "vertical"
        # header
        BoxLayout:
            size_hint: (1, None)
            height: "40dp"
            Label:
                text: "Explorar"
                halign: "left"
                valign: "middle"
                text_size: self.size
                on_touch_down: print(file_chooser_popup.pos)
                on_touch_move:print(file_chooser_popup.pos) #file_chooser_popup.pos = self.pos
            Button:
                text: 'X'
                on_press: root.close()
                size_hint: (None, 1)
                width: "60dp"
                background_color: "red"
                background_nomal: ""
                    
            
        FileChooser:
            id: fc
            rootpath: root.root_path
            #on_selection: app.selected_files(fc.selection)
            FileChooserIconLayout:
                
            FileChooserListLayout:
        BoxLayout:
            size_hint: (1, None)
            height: "40dp"

            ToggleButton:
                text: "List View"
                group: "view"
                on_release: fc.view_mode = "list"
                size_hint: (.5,1)

            ToggleButton:
                text: "Icon View"
                state: "down"
                group: "view"
                on_release: fc.view_mode = "icon"
                size_hint: (.5,1)
                        
            Button:
                text: "Ok"
                on_press: 
                    fc.on_selection = app.selected_files(fc.selection)
                    root.close()
                size_hint: (.5,1)
""")


class ModalFileChooser(ModalView):
    root_path = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.8,.8)
        if platform == "win":
            self.root_path = "C:/Users/user/Downloads"

    def close(self):
        self.dismiss()

    

