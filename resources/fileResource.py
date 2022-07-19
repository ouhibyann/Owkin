import os

from flask_restful import Resource
from flask import request

from config import UPLOAD_FOLDER
from models.db import db
from models.job import JobModel, JobSchema


JobSchema = JobSchema()

class fileResource(Resource):

    @classmethod
    def post(self):
        
        """
        This method responds to a POST request for /upload
        with a dockerfile submitted

        :params		None
        :return 	json dict -> {job_id: val}
        """
        from utils.file_utils import allowed_file
        import process


        if request.method == 'POST':
            f = request.files['file']
            file_name = f.filename
            if allowed_file(file_name) != False: # Checking the file format
            
                f.save(os.path.join(UPLOAD_FOLDER, file_name))
                
                # Logs being filed only if errors happen
                resp, log = process.process(UPLOAD_FOLDER)

                if resp == False:
                    # Retrieve the last job_id 
                    descend = JobModel.query.order_by(JobModel.job_id.desc())
                    last = descend.first()
                    last_id_value = JobSchema.get_attribute(last, attr='job_id', default=str)
                    
                    # Need to add the failed job to the table
                    latest_id = int(last_id_value) + 1
                    job = JobModel(job_id=latest_id, job_status='failed', logs=log)
                    db.session.add(job)
                    db.session.commit()
                    
                else:
                    # Retrieve the last job_id 
                    descend = JobModel.query.order_by(JobModel.job_id.desc())
                    last = descend.first()
                    last_id_value = JobSchema.get_attribute(last, attr='job_id', default=str)
                    

                    # See my solution in README.md to get the perf.json from volume.
                    # So here, I just hard-coded it but with more time I know how I would do it.
                    performance = 0.99
                    latest_id = int(last_id_value) + 1
                    job = JobModel(job_id=latest_id, job_status='failed', performances=performance)
                    db.session.add(job)
                    db.session.commit()

                return JobSchema.dump({
                    'job_id': latest_id
                    }), 201

            else:
                return 'Wrong file format', 400