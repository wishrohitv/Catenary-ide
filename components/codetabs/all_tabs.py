from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanelHeader
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty
import time
from kivy.core.window import Window

Builder.load_file("components/codetabs/all_tabs.kv")

# class AllTabs(TabbedPanel):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)       
#         self.add_widget(WelcomeTab())

#     def add_widget_(self):
#         self.add_widget(WelcomeTab())

# currently unused
# class HeaderForTabs(TabbedPanelHeader):
#     custom_tab_name = StringProperty()
#     action = ObjectProperty()
        


class WelcomeTab(TabbedPanelItem):
    greetings = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        time_ = time.localtime().tm_hour
        if  11 > time_ > 5:
            self.greetings = "Hello, Good morning😎😁😥"
        elif time_ < 13:
            self.greetings = "Hello, Good afternoon😎😁😥"
        elif time_ < 20:
            self.greetings = "Hello, Good evening😎😁😥"
        elif time_ < 24:
            self.greetings = "Hello, Good night😎😁😥"
        else:
            self.greetings = "it's time to sleep😴"
        

    # callback from header or welcome page to popup textinput
    def create_new_file_popup(self):
        from components.popuptextinput.popup_createfile_txtinput import CreatFileTextInput
        pop_box = CreatFileTextInput()
        pop_box.open_popup_textinput()


class CustomTabs(TabbedPanelItem):
    custom_tab_name = StringProperty()
    code_text = StringProperty()
    file_path = StringProperty()
    # width of x axis of code input
    initial_textinput_len_x = NumericProperty()
    
    initial_code_line = NumericProperty()
    current_code_line = NumericProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def close_tab(self, value, custom_tab):
    #     try:
    #         self.parent.remove_widget(custom_tab)
    #     except:
    #         pass
        
    # update every new line counter
    def _on_text(self, instance):
        nums = instance.text.split("\n")

        # updating current number
        self.current_code_line = len(nums)

        if self.initial_code_line < self.current_code_line:
            # self.ids.code_line_counter_container.clear_widgets()


            # for i in range(1, self.current_code_line+1):
            #     self.ids.code_line_counter_container.add_widget(CodeLineCounter(row_number_counter_for_code=i))
            self.ids.code_line_counter_container.add_widget(CodeLineCounter(row_number_counter_for_code=self.current_code_line))
            
            # updating initial number
            self.initial_code_line = len(nums)

            # removing numbers if deleted
        if self.current_code_line > self.initial_code_line:
            # updating initial number
            # self.initial_code_line = len(nums)
            print(self.initial_code_line, self.current_code_line)

            self.ids.code_line_counter_container.clear_widgets()


    # when file intilize 
    def on_kv_post(self, base_widget):
        code_lines = base_widget.ids.code_input.text
        nums = code_lines.splitlines()
        self.initial_code_line = len(nums)

        for i in range(1, self.initial_code_line + 1):
            self.ids.code_line_counter_container.add_widget(CodeLineCounter(row_number_counter_for_code=i))
        
        Clock.schedule_once(self.focus_cursor, .3)

    def focus_cursor(self, dt):
        self.ids.code_input.focus = True


    def update_textinput_width(self, instance, text_width):
        self.initial_textinput_len_x = self.ids.scroll_child_width.width

        if self.initial_textinput_len_x < text_width:
            self.ids.scroll_child_width.width = (Window.width + text_width) 
            self.initial_textinput_len_x = text_width
        else:
            self.ids.scroll_child_width.width = self.initial_textinput_len_x



class CodeLineCounter(ToggleButtonBehavior, Label):
    row_number_counter_for_code = NumericProperty(1)

    def on_row_number_conter_for_code(self):
        pass

class ImageTabs(TabbedPanelItem):
    image_tab_name = StringProperty()
    image_source = StringProperty()
    
class MediaTabs(TabbedPanelItem):
    media_tab_name = StringProperty()
    media_source = StringProperty()
    