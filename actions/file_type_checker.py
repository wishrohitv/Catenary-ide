import os

def get_file_type(file_path):
    if not os.path.isfile(file_path):
        return "File not found"
    
    file_name, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        return "Image"
    elif file_extension.lower() in [
        '.c', '.cpp', '.h', '.hpp', '.java', '.py', '.rb', '.pl', '.sh', '.bat',
        '.html', '.css', '.js', '.php', '.asp', '.aspx', '.jsp', '.xml', '.json',
        '.yaml', '.yml', '.ini', '.cfg', '.log', '.sql', '.md', '.markdown', '.rst','.txt','.text'
    ]:
        return "Text_lang"
    elif file_extension.lower() in ['.mp3', '.wav', '.flac']:
        return "Audio"
    elif file_extension.lower() in ['.mp4', '.avi', '.mov']:
        return "Video"
    else:
        return "Unknown"

