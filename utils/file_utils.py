

from click import FileError

ALLOWED_FILES = {'Dockerfile'}


def allowed_file(filename):
    """
    Checking the file submited to the service as we expect only dockerfile

    :params     filename -> explicitly only dockerfile
    :return     boolean
    """
    
    if filename in ALLOWED_FILES:
        return True
    else:
        return FileError
    
