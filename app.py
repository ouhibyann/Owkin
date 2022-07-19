import os 
import json

from flask import Flask, request

from utils.file_utils import allowed_file
from models.db import db
import process
from models.job import JobModel, JobSchema


f = open('config.json')
dict = json.load(f)
f.close()
UPLOAD_FOLDER = dict['UPLOAD_FOLDER']
POSTGRESQL_URL = dict['POSTGRESQL_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = dict['SQLALCHEMY_TRACK_MODIFICATIONS']


app = Flask(__name__)
db.init_app(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

JobSchema = JobSchema()


@app.route('/upload', methods = ['POST'])
def upload_file_api():
	
	"""
	This method responds to a POST request for /upload
	with a dockerfile submitted

	:params		None
	:return 	json dict -> {job_id: val}
	"""

	if request.method == 'POST':
		f = request.files['file']
		file_name = f.filename
		if allowed_file(file_name) != False: # Checking the file format
		
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
			
			# Logs being filed only if errors happen
			resp, log = process.process(UPLOAD_FOLDER)

			if resp == False:
				# Retrieve the last job_id 
				descend = JobModel.query.order_by(JobModel.job_id.desc())
				last = descend.first()
				resp_dict = JobSchema.dump(last)
				
				# Need to add the failed job to the table
				latest_id = int(resp_dict['job_id']) + 1
				job = JobModel(job_id=latest_id, job_status='failed', logs=log)
				db.session.add(job)
				db.session.commit()
				
			else:
				# Retrieve the last job_id 
				descend = JobModel.query.order_by(JobModel.job_id.desc())
				last = descend.first()
				resp_dict = JobSchema.dump(last)

				# See my solution in README.md to get the perf.json from volume.
				# So here, I just hard-coded it but with more time I know how I would do it.
				performance = 0.99
				latest_id = int(resp_dict['job_id']) + 1
				job = JobModel(job_id=latest_id, job_status='failed', performances=performance)
				db.session.add(job)
				db.session.commit()

			return JobSchema.dump({
				'job_id': latest_id
				}), 201

		else:
			return 'Wrong file format', 400


@app.route('/job/<int:id>', methods = ['GET', 'DELETE'])
def get_job(id):

	"""
	This method responds to a GET request for /job

	:params		id
	:return 	json dict -> db.JobModel based dict
	"""
	if request.method == 'GET':

		job = JobModel.query.get(id) # As id is the primary key, get() works well
		if job is not None:
			return JobSchema.dump(job)
		else:
			return 'Not found', 404 # Empty in base

	if request.method == 'DELETE':

		record = JobModel.query.get(id)
		if record is None:
			return 'Not found', 404
		else:
			db.session.delete(record)
			db.session.commit()
			return 'deleted', 200 # Empty in base



@app.route('/job', methods = ['POST'])
def post_job():
	"""
	This method isn't usefull for the service per se.
	However, it is usefull if you want to do some manipulation on the DB to check on how the service respond
	
	:params		json
	:return		job_id
	"""

	if request.method == 'POST':

		# get_json changed to get_data as it was causing issue with native post test
		json_data = request.get_data()
		
		if not json_data:
			return 'No input data provided', 400

		else:
			data = JobSchema.loads(json_data)
			
			job_id = JobModel.query.get(data['job_id'])
			exist = JobSchema.dump(job_id)
			if exist:
				return 'Job already exist', 400

			job = JobModel(
				job_id=data['job_id'],
				job_status=data['job_status'],
				docker_image_id=data['docker_image_id'],
				performances=data['performances'],
				logs=data['logs'])

			db.session.add(job)
			db.session.commit()

		return 'job created', 201

	
if __name__ == "__main__":               
		app.run(host='127.0.0.1',port = 5000)