from flask_restful import Resource
from flask import request

from models.db import db
from models.job import JobModel, JobSchema


JobSchema = JobSchema()

class jobResource(Resource):

    @classmethod
    def get(self, id):
        """
        This method responds to a GET / POST request for /job/<int:id>

        :params		id
        :return 	json dict -> db.JobModel based dict
        """
        job = JobModel.query.get(id) # As id is the primary key, get() works well
		
        if job is not None:
            return JobSchema.dump(job)
		
        else:
            return 'Not found', 404 # Empty in base


    @classmethod
    def delete(self, id):

        record = JobModel.query.get(id)

        if record is None:
            return 'Not found', 404

        else:
            db.session.delete(record)
            db.session.commit()
            return 'deleted', 200 # Empty in base


    @classmethod
    def post(self):
        """
        This method isn't usefull for the service per se.
        However, it is usefull if you want to do some manipulation on the DB to check on how the service respond
        
        :params		json
        :return		job_id
        """
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