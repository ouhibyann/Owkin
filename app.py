import os 
import json

from flask import Flask, request
#from utils import allowed_file
import job


UPLOAD_FOLDER = 'tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods = ['POST'])
def upload_file_api():
	"""
	This method responds to a POST request for /upload
	with a dockerfile submitted

	:params		None
	:return 	json dict -> {job_id: val, job_status: val}
	"""

	if request.method == 'POST':
		f = request.files['file']
		file_name = f.filename
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
		
		resp = job.process(UPLOAD_FOLDER)
		

		return json.dumps(resp)
		

@app.route('/job/<id>', methods = ['GET'])
def get_job(id):

	return 


if __name__ == "__main__":               
		app.run(host='127.0.0.1',port = 5000)