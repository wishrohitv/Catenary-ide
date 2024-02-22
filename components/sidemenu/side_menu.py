from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.uix.label import Label
import os, json

from actions.explorer_managment import create_file_tree

Builder.load_file("components\sidemenu\side_menu.kv")


class SideMenu(BoxLayout):
    __events__ = ('on_left_tab_state',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def left_tab_state(self, instance):
        self.dispatch('on_left_tab_state', instance)

    def on_left_tab_state(self, instance):
        pass

    def app_info_open(self):
        from components.modalview.about_modal import AboutModal
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


class FileNameLabel(ToggleButtonBehavior, Label):
    file_and_folders_name = StringProperty()


class FoldersNameLabel(TreeView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.root.text = "rohit"
        # self.root_options=dict(text='Tree One')
        self.hide_root=False
        self.indent_level=18
        folder_path = "./dummy_files"
        self.hide_root = True
        with open("tree.json") as f:
            folder_tree = json.load(f)
        self.populate_file_tree(None, folder_tree)
    

    def populate_file_tree(self, parent, folder_tree):
        if parent is None:
            tree_node = self.add_node(CustomTreeNode(file_and_folders_name=folder_tree["name"]))

        else:
            tree_node = self.add_node(CustomTreeNode(file_and_folders_name=folder_tree["name"]), parent)

        for child_node in folder_tree["children"]:
            self.populate_file_tree(tree_node, child_node)


        
# currentaly unused
class CustomTreeNode(FileNameLabel, TreeViewNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.even_color = [0,0,0,0]
        self.color_selected = [0,0,0,0]
