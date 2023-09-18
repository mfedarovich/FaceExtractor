import os
import fnmatch

def find_files(directory_path, file_extensions=['.jpg', '.png', '.gif', '.jpeg']):
    for root_dir, dir_names, file_names in os.walk(directory_path):
        for extension in file_extensions:
            for filename in fnmatch.filter(file_names, '*' + extension):
                yield os.path.join(root_dir, filename)


def get_filename_and_extension(file_path):
    base_name = os.path.basename(file_path)
    file_name, extension = os.path.splitext(base_name)
    return file_name, extension

def join_folders(root, subfolder):
    return root + subfolder

def combine(root, filename, extension) :
    return os.path.join(root, filename+extension)

def get_subfolder(base_path, path_to_file) :
    dir = os.path.dirname(path_to_file)
    return dir[len(base_path):]


def create_if_not_exist(dir) :
    if os.path.isdir(dir)==False:
         os.makedirs(dir, exist_ok=True)
