
from flask import Flask
from flask_restful import Api

from config import UPLOAD_FOLDER, POSTGRESQL_URL, SQLALCHEMY_TRACK_MODIFICATIONS
from models.db import db
from resources.jobResource import jobResource
from resources.fileResource import fileResource


app = Flask(__name__)
api = Api(app)
db.init_app(app)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS


api.add_resource(jobResource, '/job/<int:id>',
										'/job')
api.add_resource(fileResource, '/upload')


if __name__ == "__main__":               
	app.run(host='127.0.0.1', port = 5000, debug=True)