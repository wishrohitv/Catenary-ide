from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

Builder.load_string("""

<CreatFileTextInput>:
    size_hint_y: None
    height: "40dp"
    pos_hint: {'center_y': .5}
    spacing: 3
    padding: 1
                    

    TextInput:
        id: file_name
        hint_text: "enter file name"
        text: "catxcode.txt"
        cursor_color: 0,1,0,1
        cursor_width: "4sp"
        foreground_color: (247/255,9/255,211/255,1)
        font_size: 20
        multiline: False
        selection_color: 1,0,1,.23
        background_color: .4,.01,.4,.5
        background_normal: ''
        on_text_validate: 
            app.save_text_file(file_name.text)
            root.close_popup_textinput()
        # canvas.before:
        #     Color:
        #         rgba: (1,1,1,.3)
        #     RoundedRectangle:
        #         pos: self.pos
        #         size: self.size
        #         radius: [2]
    Button:
        text: "create"
        font_size: 20
        background_color: "purple"
        background_normal: ''
        size_hint_x: .23
        on_press: 
            app.save_text_file(file_name.text)
            root.close_popup_textinput()
        # canvas.before:
        #     Color:
        #         rgba: (0,1,0,1)
        #     RoundedRectangle:
        #         pos: self.pos
        #         size: self.size
        #         radius: [2]


""")

class CreatFileTextInput(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.popup = None

    def open_popup_textinput(self):
        self.popup = Popup(title='Create file', 
                            title_color="green", 
                            title_size=18,
                            content=self,
                            auto_dismiss=True, 
                            size_hint=(.45, .21), 
                            separator_color="purple", 
                            background_color=(0,0,1,1))

        self.popup.open()
        Clock.schedule_once(self.focus_text_input, 0.3)

    def close_popup_textinput(self):
        self.popup.dismiss()
        

    def focus_text_input(self, dt):
        self.ids.file_name.focus = True
