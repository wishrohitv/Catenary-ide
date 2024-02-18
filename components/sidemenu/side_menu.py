from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.factory import Factory

Builder.load_file("components\sidemenu\side_menu.kv")


class SideMenu(BoxLayout):
    def app_info_open(self):
        from components.modalview.about_modal import AboutModal
        Factory.AboutModal().open()


class LeftTabs(ToggleButtonBehavior, Image):
    pass

class SideMenuTabWindows(BoxLayout):
    pass