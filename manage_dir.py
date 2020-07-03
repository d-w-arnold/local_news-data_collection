import os
import shutil


def del_dir_contents(path):
    print("** Deleting files/directories in: {} **".format(path))
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print("** Deleted file: {} **".format(file_path))
        except Exception as e:
            print("** Failed to delete ** : {0} - Reason: {1}".format(file_path, e))


def prepare_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(path):
        del_dir_contents(path)
    else:
        os.mkdir(path)
