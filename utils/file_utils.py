
ALLOWED_FILES = {'Dockerfile'}


def allowed_file(filename) -> bool:
    """
    Checking the file submited to the service as we expect only dockerfile

    :params     filename -> explicitly only dockerfile
    :return     boolean
    """
    
    if filename in ALLOWED_FILES:
        return True
    else:
        return False
    