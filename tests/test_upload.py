import unittest

import app
from models.job import JobModel, JobSchema
from models.db import db


class UploadTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.db = db.init_app(self.app)


    def test_successful_upload(self):
        """
        Testing if the upload of the Dockerfile is a success
        The job_status (success / fail) is irrevelant for this test
        Change the path in 'filePath_test.txt' to test a different file
        """
        

    def test_failed_upload(self):
        """
        Testing if the upload failed due to wrong file submitted
        Change the path in 'filePath_test.txt' to test a different file
        """
        

