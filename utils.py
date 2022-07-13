

from click import FileError
from numpy import true_divide

ALLOWED_FILES = {'Dockerfile'}


def allowed_file(filename):
    '''
    input: filename -> explicitly only dockerfile
    output: boolean
    '''
    if filename in ALLOWED_FILES:
        return True
    else:
        return FileError
    
