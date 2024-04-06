from kivy.utils import platform
file_name_and_path_dict = {}
def file_name_(file_path):
    if platform == "win":

        file_name_extracted = file_path.split("\\")[-1]

        file_name_and_path_dict["file_name"] = file_name_extracted
        file_name_and_path_dict["file_path"] = file_path
        return file_name_and_path_dict
    else:
        file_name_extracted = file_path.split("/")[-1]

        file_name_and_path_dict["file_name"] = file_name_extracted
        file_name_and_path_dict["file_path"] = file_path
        return file_name_and_path_dict