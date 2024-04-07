from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.clock import Clock, mainthread
from kivy.core.window import Window
from plyer import filechooser
import threading, time, asyncio, os
from kivy.app import App

from components.sidemenu.side_menu import SideMenu


class EditorApp(App):
    console_open = True

    def build(self):
        # front ui
        self.title = "CodeEditor"
        self.icon = "assets/icons/icon-x.jpg"

        return Builder.load_file("main.kv")

    def on_start(self):
        Window.softinput_mode = 'below_target'

    # code logic starts here --
    def __init__(self, **args):
        super(EditorApp, self).__init__(**args)
        self.engine = None
        self.current_active_tabs = []

    # side tabs state mananger if tab is opend or not
    def on_left_tab_state(self, instance):
        # print(instance.name, instance.state)
        side_tab_list = self.root.ids.tab_container.children
        # print(side_tab_list)

        if len(side_tab_list) == 2:
            if instance.state == "normal":
                self.root.ids.tab_container.remove_widget(self.root.ids.splliter_sidemenutabswindows)

        if len(side_tab_list) < 2:
            if instance.state == "down":
                self.root.ids.tab_container.add_widget(self.root.ids.splliter_sidemenutabswindows, 1)

    def open_console_and_close(self, instance):
        from components.terminal.py_terminal import Terminal
        tab_and_console = self.root.ids.tab_and_consle_container
        terminal_ = self.root.ids.terminal_place
        if self.console_open:
            tab_and_console.remove_widget(terminal_)
            self.console_open = False
        else:
            tab_and_console.add_widget(terminal_)
            self.console_open = True

    # update cursor line and column
    def update_bottom_header_label_cursor_point(self, pos, selected_text):
        ln, col = pos
        self.root.ids.cursor_pos.text = f'Ln {ln + 1}, Col {col + 1}'

        if len(selected_text) > 0:
            self.root.ids.selected_text.text = f"{len(selected_text)} selected"
        else:
            self.root.ids.selected_text.text = ""

    # ================================================

    # windows files state manager selection on code tabs explorer
    def explorer_tabs(self, instance):
        from actions.file_type_checker import get_file_type
        filename = instance.file_and_folders_name
        path = instance.source_path
        filenameAndPath = {"file_name": filename, "file_path": path}
        if not os.path.isdir(path):
            # self.text_lang_tab(filenameAndPath)
            match get_file_type(path):
                case "Text_lang":
                    self.text_lang_tab(filenameAndPath)
                    # t1 = threading.Thread(target=self.thredign, args=[file_name, self.file_path])
                    # t1.start()
                    # asyncio.create_task(self.text_lang_tab(file_name, self.file_path))

                case "Video":
                    self.media_tab(filenameAndPath)
                case "Image":
                    self.image_tab(filenameAndPath)
        # --------------------------------------

    # opening file from chooser
    def open_file_from_header(self):
        # filechooser.open_file(on_selection=self.selected_files)
        from components.kivyfilechooser.file_chooser import ModalFileChooser
        Factory.ModalFileChooser().open()

    def selected_files(self, file_path):
        from actions.file_type_checker import get_file_type
        from actions.filepath_spliter import file_name_

        if len(file_path) != 0:
            self.file_path = file_path[0]
            self.title = f"CatxCode {self.file_path}"

            # file name and path form filepath in dict
            file_name_and_path_dict = file_name_(self.file_path)

            # adding to tabs by checking filetype
            match get_file_type(self.file_path):
                case "Text_lang":
                    self.text_lang_tab(file_name_and_path_dict)
                    # t1 = threading.Thread(target=self.thredign, args=[file_name, self.file_path])
                    # t1.start()
                    # asyncio.create_task(self.text_lang_tab(file_name, self.file_path))

                case "Video":
                    self.media_tab(file_name_and_path_dict)
                case "Image":
                    self.image_tab(file_name_and_path_dict)

    async def my_async_function(self, file_name_and_path_dict):
        print("woohooo running async function on kivy app")
        await self.text_lang_tab(file_name_and_path_dict)

    # def thredign(self,file_name, filepath):
    #     with open(filepath) as f:
    #         content = f.read()
    #     self.text_lang_tab(file_name, content)
    # @mainthread
    def text_lang_tab(self, file_name_and_path_dict):
        from components.codetabs.all_tabs import CustomTabs
        if file_name_and_path_dict["file_path"] not in self.current_active_tabs:
            with open(file_name_and_path_dict["file_path"]) as f:
                content = f.read()
            self.root.ids.all_tabs_bar.add_widget(
                CustomTabs(custom_tab_name=file_name_and_path_dict["file_name"], code_text=content,
                           file_path=file_name_and_path_dict["file_path"]))

            self.current_active_tabs.append(file_name_and_path_dict["file_path"])

        self.switch_to_current_tab(file_name_and_path_dict)

    def media_tab(self, file_name_and_path_dict):
        from components.codetabs.all_tabs import MediaTabs, ImageTabs
        self.root.ids.all_tabs_bar.add_widget(MediaTabs(media_tab_name=file_name_and_path_dict["file_name"],
                                                        media_source=file_name_and_path_dict["file_path"]))

        self.current_active_tabs.append(file_name_and_path_dict["file_path"])
        self.switch_to_current_tab(file_name_and_path_dict)

    def image_tab(self, file_name_and_path_dict):
        from components.codetabs.all_tabs import ImageTabs
        self.root.ids.all_tabs_bar.add_widget(ImageTabs(image_tab_name=file_name_and_path_dict["file_name"],
                                                        image_source=file_name_and_path_dict["file_path"]))

        self.current_active_tabs.append(file_name_and_path_dict["file_path"])
        self.switch_to_current_tab(file_name_and_path_dict)

    # def save_file(self, args):
    #     with open(self.file_path, "w") as f:
    #         f.write(self.textinput.text)

    # new tab creater from header
    def create_new_file_from_header(self):
        from components.codetabs.all_tabs import WelcomeTab
        welcome = WelcomeTab()
        welcome.create_new_file_popup()

    def save_text_file(self, file_name):
        with open("./dummy_files/code.js", "r") as f:
            s = f.read()
            n = s.splitlines()

        from components.codetabs.all_tabs import CustomTabs
        from components.codetabs.all_tabs import CodeLineCounter

        customtabs = CustomTabs()

        # code line counter
        for i in range(len(n)):
            customtabs.ids.code_line_counter_container.add_widget(CodeLineCounter(
                row_number_counter_for_code=i))

        # tab code
        print(file_name)
        self.root.ids.all_tabs_bar.add_widget(CustomTabs(custom_tab_name=file_name, code_text=s))
        self.switch_to_current_tab()

    def switch_to_current_tab(self, file_name_and_path_dict):
        panel = self.root.ids.all_tabs_bar
        if panel.tab_list:
            # print(panel.tab_list[0].file_path)
            panel.switch_to(panel.tab_list[0])

    # close_tab
    def close_tab(self, instance, tab_id):
        self.root.ids.all_tabs_bar.remove_widget(tab_id)
        panel = self.root.ids.all_tabs_bar
        if panel.tab_list:
            panel.switch_to(panel.tab_list[0])
        else:
            panel.clear_widgets()

    # run code function
    def run_code(self):
        import subprocess
        from kivy.uix.popup import Popup

        engine_selection = self.file_path.split(".")
        print(engine_selection)
        if engine_selection[-1] == "js":
            self.engine = "node"
        elif engine_selection[-1] == "py":
            self.engine = "python"
        try:
            co = subprocess.run([self.engine, self.file_path])
            f = Label(text=str(co))
            self.popup = Popup(title='Console Output', title_color="green", title_size=18, content=f,
                               auto_dismiss=True, size_hint=(.45, .21), separator_color="purple",
                               background_color=(0, 0, 1, 1))
        except Exception as e:
            print(type(e))
            l = Label(text=str(e))
            self.popup = Popup(title='Console Output', title_color="blue", title_size=18, content=l,
                               auto_dismiss=True, size_hint=(.45, .21), separator_color="purple",
                               background_color=(0, 0, 1, 1))

        self.popup.open()


asyncio.run(EditorApp().async_run('asyncio'))
