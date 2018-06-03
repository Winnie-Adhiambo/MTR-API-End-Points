import json
import unittest
from maintenance import app

class Request_tests(unittest.TestCase):
    def setUp(self):
        app.config["Testing"] = True
        self.client = app.test_client()


    def test_hello_world(self):
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code,200)

    def test_create_request_works(self):
        request = {"title": "car", "description": "brake pads",
                   "category": "repair"}
        res = self.client.post('/api/v1/request', json=request)
        self.assertEqual(res.status_code, 201)

    def test_create_request_with_no_title(self):
        request = {"description": "brake pads",
                   "category": "repair"}
        res = self.client.post('/api/v1/request', json=request)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['message']['title'], "please enter title")

    def test_create_request_with_no_description(self):
        request = {"title": "car",
                   "category": "repair"}
        res = self.client.post('/api/v1/request', json=request)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['message']['description'], "please enter description ")

    def test_create_request_with_no_category(self):
        request = {"title": "car", "description": "brake pads"}
        res = self.client.post('/api/v1/request', json=request)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json['message']["category"], "please enter category")

    def test_update_request(self):
        request = {"title": "car", "description": "brake pads", "category": "repair"}
        res = self.client.post('/api/v1/request', json=request)
        post_id = res.json['request_id']
        request = {"title": "laptop", "description": "hard disk", "category": "repair"}
        self.client.put('/api/v1/request/' + str(post_id), json=request)
        updated = self.client.get('/api/v1/request/' + str(post_id))
        self.assertEqual(updated.json['request_title'], "laptop")
        self.assertEqual(updated.json['request_description'], "laptop harddisk repair")

    def test_get_all(self):
        request = self.client.get('/api/v1/request')
        self.assertEqual(request.status_code, 200)


if __name__ == "__main__":
    unittest.main()