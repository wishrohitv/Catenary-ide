from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.app import runTouchApp
import subprocess, os
from functools import partial

Builder.load_file("./components/terminal/py_terminal.kv")


class Terminal(BoxLayout):
    console_text = StringProperty(f"root@{os.getcwd()}$~ ")
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

        code.remove(f"root@{os.getcwd()}$~")
        # '''
        # users commands 1st index
        user_commands = code[0]

        if user_commands == "cd":
            # Change directory using os.chdir
            directory = code[1]
            os.chdir(directory)
            self.n = f"root@{os.getcwd()}$~ "
            return ""
        # '''
        else:
            try:
                s = subprocess.run(code, capture_output=True, shell=True)
                return s.stdout.decode()

            except Exception as e:
                return str(e)

# runTouchApp(Terminal())
