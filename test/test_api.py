import unittest
# import unittest framework

import os

from app import create_app
# from our app folder inside init.py get create_app method 

import json

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client()
        self.request = {'title':'car','type':'brake pads','date':'1/1/18'}
    def test_request_creation(self):
        results = self.client.post('/api/v1/request',data = json.dumps(dict(title='car',type='brake pads',date='1/1/18')),content_type = "application/json")
        response = json.load(results.data.decode())
        self.assertEqual(response.status_code,201)
        self.assertIn("Responce Created",response["message"])

    def test_api_can_get_all_requests(self):
        create = self.client.post('/api/v1/request' ,data = json.dumps(dict(request_title="car",request_type = "brake pads",request_date = "1/1/2018")),content_type = "application/json")
        res = self.client.get('/api/v1/request')
        response = json.loads(res.data.decode())
        created_request = response[0]
        self .assertEqual(created_request["request_title"],"car")

    def test_api_can_get_request_by_id(self):
        create = self.client.post('/api/v1/request',data=json.dumps(dict(request_title = "car",
        request_description="brake pads",request_date="1/1/18")),content_type="application/jason")
        result = self.client.get('/api/v1/request/0')
        response = json.loads(results.data.decode())
        self.assertIn("brake pads",response["request_description"])

    def test_api_can_update_requests(self):
        request = self.client.post('api/v1/request/0',data-json.dumps(dict(request_title-"car",
        request_description="brake pads",request_category = 'date')), content_type = "application/json")
        response = self.client.put('api/v1/request/o' , data=json.dumps(dict(request_title="car",request_description ="",
        request_category = "car")),content_type="application/json")
        result = self.client.get9('/api/v1/request/0')
        self.assertIn("computer",response["title"])

    def test_add_empty_request_description(self):
        create = self.client.post('/api/v1/request',data = json.dumps(dict(request_title="car",request_description=""
        ,request_category="car")),content_type = "application/json")
        result = json.loads(create.data.decode()) 
        self.assertin("request_description is required" , res['message'])

    def test_add_empty_request_title(self):
        create = self.client.post('api/v1/request',data=json.dumps(dict(request_title="car",request_description="brake pad repaire",
        request_category="")),content_type = "application/json")
        result = json.loads(create.data.decode())
        self.assertIn("request_category is required",res['message'])

    def test_add_invalid_request_id(self):
        create = self.client.get('api/v1/requests/5')
        result = json.loads(create.data.decode())
        self.assertIn("id not found",result['message'])

    if __name__ == "__main__":
        Unittest.main()


