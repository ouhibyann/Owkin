

from click import FileError
from numpy import true_divide


def allowed_file(filename):
    '''
    input: filename -> explicitly only dockerfile
    output: boolean
    '''
    if filename == 'dockerfile':
        return True
    else:
        return 'Wrong file format' + FileError
    
