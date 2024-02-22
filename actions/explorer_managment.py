import os, json, time

def create_file_tree(folder_path):

    file_tree = {"name": os.path.basename(folder_path)}
    if os.path.isdir(folder_path):
        file_tree["type"] = "folder"
        file_tree["children"] = [
            create_file_tree(os.path.join(folder_path, f)) for f in os.listdir(folder_path)
        ]
    else:
        file_tree["children"] = []
    return file_tree

folder_path = "./dummy_files"
file_tree = create_file_tree(folder_path)
with open("tree.json", "w") as f:
    json.dump(file_tree, f)

