import os 

from flask import Flask, request

from utils import allowed_file
from models.job import Job
import process


UPLOAD_FOLDER = 'tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods = ['POST'])
def upload_file_api():
	"""
    This function responds to a POST request for /upload
    with a Dockerfile submitted

    :param job_id:	None
    :return:	person matching ID
    """
	if request.method == 'POST':
		f = request.files['file']
		file_name = f.filename

		# Checking the file format, a response is sent from the function return if wrong format
		allowed = allowed_file(file_name)
		if allowed != True:
			return allowed

		f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
		# print(str(UPLOAD_FOLDER + '\\' + file_name))
		resp = process.flow(str(UPLOAD_FOLDER + '\\' + file_name))

		return resp
		

@app.route('/job/<id>', methods = ['GET'])
def get_job_api(job_id):
	"""
    This function responds to a GET request for /job/{job_id}
    with one matching job from all jobs.

    :param job_id:	ID of person to find
    :return:	person matching ID
    """
	

	return json.dumps({

	}) 


if __name__ == "__main__":               
		app.run(host='127.0.0.1',port = 5000)