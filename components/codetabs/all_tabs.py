from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanelHeader
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty

Builder.load_file("components/codetabs/all_tabs.kv")


# class AllTabs(TabbedPanel):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)       
#         self.add_widget(WelcomeTab())

#     def add_widget_(self):
#         self.add_widget(WelcomeTab())

class HeaderForTabs(TabbedPanelHeader):
    custom_tab_name = StringProperty()
    action = ObjectProperty()
        


class WelcomeTab(TabbedPanelItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # callback from header or welcome page to popup textinput
    def create_new_file_popup(self):
        from components.popuptextinput.popup_createfile_txtinput import CreatFileTextInput
        pop_box = CreatFileTextInput()
        pop_box.open_popup_textinput()


class CustomTabs(TabbedPanelItem):
    custom_tab_name = StringProperty()
    code_text = StringProperty()
    existing_code_lines = NumericProperty()
    new_code_lines = NumericProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def close_tab(self, value, custom_tab):
    #     try:
    #         self.parent.remove_widget(custom_tab)
    #     except:
    #         pass
        
    # update every new line counter
    def _on_text(self, instance):
        nums = instance.text.splitlines()
        self.new_code_lines = len(nums)
        # print(self.new_code_lines)

        if self.existing_code_lines < self.new_code_lines:
            self.ids.code_line_counter_container.add_widget(CodeLineCounter(row_number_counter_for_code=self.new_code_lines), -1)
            print(self.new_code_lines)


    # when file intilize 
    def on_kv_post(self, base_widget):
        code_lines = base_widget.ids.code_input.text
        nums = code_lines.splitlines()
        self.existing_code_lines = len(nums)

        for i in range(1, self.existing_code_lines + 1):
            self.ids.code_line_counter_container.add_widget(CodeLineCounter(row_number_counter_for_code=i))
        
        Clock.schedule_once(self.focus_cursor, .3)

    def focus_cursor(self, dt):
        self.ids.code_input.focus = True



class CodeLineCounter(ToggleButtonBehavior, Label):
    row_number_counter_for_code = NumericProperty(1)

    def on_row_number_conter_for_code(self):
        pass
    # def on_kv_post(self, base_widget):
    #     print(base_widget, "rohit", self)



        