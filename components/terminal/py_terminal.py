import os
import subprocess
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_file("./components/terminal/py_terminal.kv")


class Terminal(BoxLayout):
    console_text = StringProperty(f"root@{os.getcwd()}$~ ")
    initial_textinput_len_x = NumericProperty()

    # n = "root@user$~ "
    n = f"root@{os.getcwd()}$~ "

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _on_text_validate(self, instance):
        instance.text = instance.text + "\n" + self.run_commands(instance) + "\n" + self.n

    def run_commands(self, cm):
        raw_cm = cm.text
        all_line = raw_cm.split("\n")
        last_line = all_line[-1]

        code = last_line.split(" ")
        try:
            code.remove(f"root@{os.getcwd()}$~")
        except Exception as e:
            return str(e)
        # '''
        # users commands 1st index to change directory
        user_commands = code[0]

        if user_commands == "cd":
            try:
                # Change directory using os.chdir
                print(len(code))
                if len(code) > 1:
                    print(True)
                    directory = code[1]
                    os.chdir(directory)
                    self.n = f"root@{os.getcwd()}$~ "
                    return ""
                else:
                    try:
                        target_dir = code[0]
                        os.chdir(target_dir)
                        print("done")
                        return "done"
                    except Exception as e:
                        print(e)
                        return str(e)

            except Exception as e:
                print(e)
                return str(e)
        # '''
        else:
            try:
                s = subprocess.run(code, stdout=subprocess.PIPE, universal_newlines=True, text=True)
                Clock.schedule_once(self.focus_terminal, 0.3)
                return s.stdout

            except Exception as e:
                Clock.schedule_once(self.focus_terminal, 0.3)
                return str(e)

    def focus_terminal(self, dt):
        self.ids.console.focus = True

    def update_textinput_width(self, instance, textinput_width, text_width):
        self.initial_textinput_len_x = textinput_width

        if self.initial_textinput_len_x < text_width:
            instance.width = (Window.width + text_width)
            self.initial_textinput_len_x = text_width
        else:
            instance.width = self.initial_textinput_len_x

# runTouchApp(Terminal())
