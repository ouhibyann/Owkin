import json

f = open('config.json')
dict = json.load(f)
f.close()
UPLOAD_FOLDER = dict['UPLOAD_FOLDER']
POSTGRESQL_URL = dict['POSTGRESQL_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = dict['SQLALCHEMY_TRACK_MODIFICATIONS']
CONTAINER_LIMIT = dict['CONTAINER_LIMIT']