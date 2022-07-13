import os 

from flask import Flask, request
#from utils import allowed_file
from process import build, create_volume


UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():

	if request.method == 'POST':
		f = request.files['file']
		file_name = f.filename
		f.save(file_name)
		
		path = os.path.abspath(file_name)
		dir = os.path.dirname(path)
		
		build(dir)
		return 'Container built'
		


if __name__ == "__main__":               
		app.run(host='127.0.0.1',port = 5000)