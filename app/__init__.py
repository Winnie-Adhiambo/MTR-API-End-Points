from flask import Flask
from flask_restful import Api

from app.Request import HelloWorld, RequestById, RequestAll

app = Flask(__name__)
api = Api(app)
api.add_resource(HelloWorld,'/')
api.add_resource(RequestById, '/api/v1/request/<int:id>', endpoint = 'requestbyid')
api.add_resource(RequestAll, '/api/v1/request', endpoint = 'requestall')
