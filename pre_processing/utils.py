import os


def check_exist_folder(path):
    '''Check if the directory exists or not?
    Args:
      - path: path to directory
    Returns:
      - if directory is not exists, the new folder was created
    '''
    if not os.path.exists(path):
        os.makedirs(path)