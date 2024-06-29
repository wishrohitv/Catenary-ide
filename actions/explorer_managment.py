import os, json, time
from kivy.utils import platform
from app_storage_implement.app_storage import storage_path


def create_file_tree(folder_path):
    file_tree = {"name": os.path.basename(folder_path)}
    if os.path.isdir(folder_path):
        file_tree["type"] = "folder"
        file_tree["source_path"] = f"{(folder_path)}"
        file_tree["children"] = [
            create_file_tree(os.path.join(folder_path, f)) for f in os.listdir(folder_path)
        ]
    else:
        file_tree["type"] = "file"
        file_tree["children"] = []
        file_tree["source_path"] = f"{(folder_path)}"
    return file_tree


if platform == "win" or platform == "linux" or platform == "macosx":
    # folder_path = "C:\\Users\\user\\CatxCode-ide"
    folder_path = storage_path
elif platform == "android":
    # folder_path = "/storage/emulated/0/"
    folder_path = storage_path

file_tree = create_file_tree(folder_path)
with open("tree.json", "w") as f:
    json.dump(file_tree, f)
