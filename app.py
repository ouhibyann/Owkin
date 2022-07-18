import os 
import json

from flask import Flask, request

#from utils import allowed_file
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
	:return 	json dict -> {job_id: val, job_status: val}
	"""

	if request.method == 'POST':
		f = request.files['file']
		file_name = f.filename

		# Checking the file format, a response is sent from the function return if wrong format
		#allowed = allowed_file(file_name)

		f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
		
		resp = process.process(UPLOAD_FOLDER)
		if resp == False:
			# Retrieve the last job_id 
			descend = JobModel.query.order_by(JobModel.job_id.desc())
			last = descend.first()
			resp_dict = JobSchema.dump(last)
			
			# Need to add the failed job to the table
			latest_id = int(resp_dict['job_id']) + 1
			job = JobModel(job_id=latest_id, job_status='failed')
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
			})


@app.route('/job/<int:id>', methods = ['GET'])
def get_job(id):

	if request.method == 'GET':
		job = JobModel.query.get(id) # As id is the primary key, get() works well

		return JobSchema.dump(job)


if __name__ == "__main__":               
		app.run(host='127.0.0.1',port = 5000)