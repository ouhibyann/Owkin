import json
import unittest

import app

'''
The following file if is not working due to error import, please move it out of the 'test' module
It might be due to your pythonpath - As I had this issue.
---------------------
-> Found out the command to run test inside package:  python -m unittest discover -p 'test_job.py'
-> Modified delete test with correct URL
'''
class JobTest(unittest.TestCase):


    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

      
    # I know the other test cases are failing because of the 'self.client.post()' failling but not finding out why
    def test_successful_post_job(self):
        """
        Testing with a successful json sent
        """
        self.client.delete('/job/999')
        test_data = {"job_id": 999, "job_status": "success", "docker_image_id": "", "performances": 0.9, "logs": {}}
        
        res = self.client.post('/job', json=test_data)
        self.assertEqual(res.status_code, 201)


    def test_already_exist_post_job(self):
        """
        Testing with a json containing already existing data
        Expecting a 400
        """
        test_data = {"job_id": 999, "job_status": 'success', "docker_image_id": "", "performances": 0.9, "logs": {}}
       
        self.client.post('/job', json=test_data)
        res = self.client.post('/job', json=test_data) # duplicate

        self.assertEqual(res.status_code, 400)


    def test_failed_get_job(self):
        """
        Testing a failed get from a job in test DB - id doesn't exist
        Adding a job to the DB first - in case it's empty.
        Retrieving it from the API where we check the status and content
        """
        self.client.delete('/job/999')

        res = self.client.get('/job/999')
        self.assertEqual(res.status_code, 404)


    def test_successful_get_job(self):
        """
        Testing a successful get from a job in test DB
        Adding a job to the DB first - in case it's empty.
        Retrieving it from the API where we check the status and content
        """
        test_data = {"job_id": 999, "job_status": 'success', "docker_image_id": "", "performances": 0.9, "logs": {}}
        self.client.post('/job', json=test_data)

        res = self.client.get('/job/999')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.data), test_data)


    def test_failed_delete_job(self):
        """
        Deleting a ressource not existing
        """
        self.client.delete('/job/999') # To be sure the ressource doesn't exist
        
        res = self.client.delete('/job/999')
        self.assertEqual(res.status_code, 404)

    
    def test_successful_delete_job(self):
        """
        Deleting a ressource we just created
        """
        test_data = {"job_id": 999, "job_status": 'success', "docker_image_id": "", "performances": 0.9, "logs": {}}
        self.client.post('/job', json=test_data)

        res = self.client.delete('/job/999')
        self.assertEqual(res.status_code, 200)


# python -m unittest discover -p 'test_job.py'