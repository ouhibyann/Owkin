import unittest
import io

import app
from models.job import JobModel, JobSchema
from models.db import db


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.db = db.init_app(self.app)


    def test_wrong_file_upload(self):
        """
        Testing if the upload failed due to wrong file submitted
        Change the path in 'filePath_test.txt' to test a different file
        """
        test_data = {
            'file': (io.BytesIO(b"some initial text data"), "fake-text-stream.txt")
        }

        res = self.client.post('/upload', data=test_data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'Wrong file format')


    def test_successful_upload(self):
        """
        Testing if the upload of the Dockerfile is a success
        The job_status (success / fail) is irrevelant for this test
        Also, whatever is inside the dockerfile doesn't matter as it's unit test
        Change the path in 'filePath_test.txt' to test a different file
        """
        test_data = {
            'file': (io.BytesIO(b"FROM ubuntu:latest"), "Dockerfile")
        }
        
        res = self.client.post('/upload', data=test_data)
        self.assertEqual(res.status_code, 201)
            

# python -m unittest discover -p 'test_upload.py'