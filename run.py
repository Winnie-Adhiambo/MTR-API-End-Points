from flask import Flask
from flask_restful import Api
from app.Request import RequestById,RequestAll

app = Flask(__name__)
api = Api(app)

#we determine these endpoints below after writting our class in request.py
api.add_resource(RequestById,'/api/v1/request/<int:id>', endpoint = 'requestbyid') 
api.add_resource(RequestAll,'/api/v1/request', endpoint = 'requestall')

if __name__ == '__main__':
    app.run(debug=True) 