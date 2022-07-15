import os 

from flask import Flask, request
#from utils import allowed_file

import job


UPLOAD_FOLDER = 'tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():

	if request.method == 'POST':
		f = request.files['file']
		file_name = f.filename
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
		
		
		# To be executed like an external service
		resp = job.process(UPLOAD_FOLDER)

		return resp
		

if __name__ == "__main__":               
		app.run(host='127.0.0.1',port = 5000)