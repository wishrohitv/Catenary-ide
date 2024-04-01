from kivy.utils import platform

def file_name_(file_path):
    if platform == "win":
        return file_path.split("\\")
    else:
        return file_path.split("/")