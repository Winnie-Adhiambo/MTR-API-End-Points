from flask import Flask, jsonify, request
# import flask 

from flask_restful import Api, Resource, reqparse
# import restful

from instance.config import app_config
# from our instance folder ger config .py and give us variable app_config
from app.models import Request, request_store

def create_app (config_name):
# creates an instance of the application and configures it
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    request = Request("car","breakpad","1/1/18")
    request = request.add_request()
    @app.route('/user/request', methods=['GET'])
    def get_all_request():
        return jsonify({"request":requests})
    return app

    



