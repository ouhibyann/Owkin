from models.db import db, ma
from marshmallow import fields

class JobModel(db.Model):

    __tablename__ = 'Jobs'
    
    job_id = db.Column(db.Integer, primary_key=True)
    job_status = db.Column(db.String(128))
    docker_image_id = db.Column(db.Integer)
    performances = db.Column(db.Float)
    logs = db.Column(db.JSON)

    def __init__(self, job_id, job_status, docker_image_id, performances, logs) -> None:
        super().__init__()
        self.job_id = job_id
        self.job_status = job_status
        self.docker_image_id = docker_image_id
        self.performances = performances
        self.logs = logs


class JobSchema(ma.Schema):
    job_id = fields.Integer()
    job_status = fields.String()
    docker_image_id = fields.String()
    performances = fields.Float()
    logs = fields.Dict()