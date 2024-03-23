from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.properties import StringProperty, ColorProperty
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.uix.label import Label
import os, json

from actions.explorer_managment import create_file_tree

Builder.load_file("./components/sidemenu/side_menu.kv")


class SideMenu(BoxLayout):
    __events__ = ('on_left_tab_state',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def left_tab_state(self, instance):
        self.dispatch('on_left_tab_state', instance)

    def on_left_tab_state(self, instance):
        pass

    def app_info_open(self):
        from components.aboutmodal.about_modal import AboutModal
        Factory.AboutModal().open()

class LeftTabs(ToggleButtonBehavior, Image):
    pass

class SideMenuTabWindows(BoxLayout):
    file_name = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # found an error that, some time init can't recognize its childer widget by id

    # def on_kv_post(self, base_widget):
    #     list_of_files = explorer_managment(3, 1)
    #     for files in list_of_files:
    #         self.ids.explorer_tabs.add_widget(FileNameLabel(file_and_folders_name=files))

# files and folder in explorar
class FileNameLabel(ToggleButtonBehavior, BoxLayout): # also for folder
    file_and_folders_icon = StringProperty("python.png")
    file_and_folders_name = StringProperty()


class FoldersNameLabel(TreeView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.root.text = "rohit"
        # self.root_options=dict(text='Tree One')
        self.indent_level=18
        folder_path = "./dummy_files"
        self.hide_root = True
        with open("tree.json") as f:
            folder_tree = json.load(f)
        self.populate_file_tree(None, folder_tree)

    # def select_node(self, node):
    #     print(node.text)
        lang_icon_list = ['py', 'c', 'c++','cpp', 'cxx', 'js', 'java']
        
    

    def populate_file_tree(self, parent, folder_tree):
        # , color=[1,0,0,1] if folder_tree["type"] == "folder" else [0,1,0,1]
        if parent is None:
            tree_node = self.add_node(CustomTreeNode(file_and_folders_name=folder_tree["name"], file_and_folders_icon="folder.png"))

        else:
            tree_node = self.add_node(CustomTreeNode(file_and_folders_name=folder_tree["name"], file_and_folders_icon="folder.png" if folder_tree["type"] == "folder" else self.file_icon(folder_tree["name"])), parent)

        for child_node in folder_tree["children"]:
            self.populate_file_tree(tree_node, child_node)

    def file_icon(self, file_name):
        file = file_name.split(".")[-1]
        match file:
            case "js":
                return "js.png"
            case "asm":
                return "file.png"
            case "c":
                return "c-.png"
            case "java":
                return "java.png"
            case "py":
                return "python.png"         
        return "file.png"
        
# currentaly unused
class CustomTreeNode(FileNameLabel, TreeViewNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.even_color = [0,1,0,0]
        self.color_selected = [75/255, 53/255, 78/255, .7]
