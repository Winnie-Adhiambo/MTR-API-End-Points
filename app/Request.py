

from flask_restful import Resource
from flask_restful import fields,marshal_with
from flask_restful import abort
from flask_restful import reqparse



# this is where your models go



# class requestsDao,   DAO(Data Access Object)this is for creating and storing our data
class RequestDao(object):
    
    def __init__(self,id,title,description,category,):#here we are initializing respective data objects to be accessed in respective order
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        

request_store = []#this is where we store our data to be accessed by the methods
request_store.append(RequestDao(id = 1,title = 'car',description = 'brake pads repair',category = 'repair'))
request_store.append(RequestDao(id = 2,title = 'laptop',description = 'hard disk repair',category = 'repair'))
request_store.append(RequestDao(id = 3,title = 'software',description = 'softwaire update',category = 'repair'))

resource_fields = {'id':fields.Integer,'title':fields.String,'description':fields.String,'category':fields.String}
#resource_field  lists the properties of the information returned by the endpoint

reqparse = reqparse.RequestParser()#reqparse is a second stage validation process ,from marshal_with,which ensure the request  observes to the respective argument
reqparse.add_argument('title',type=str,required=True, help='No Title Given',location='json')
reqparse.add_argument('description',type=str,required=True, help='No description Given',location='json')
reqparse.add_argument('category',type=str,required=True, help='No category Given',location='json')

class RequestById(Resource):
    #this class includes only the get by id and put methods which have a unique id.
    @marshal_with(resource_fields)
    #@marshal_with filters the data in resource fields to ensure its in right format e.g string,integer.
    def get(self,id):
    #this is get method that request data with an id, i.e data already processed, from request store.
        for request in request_store:
            if (request.id == id):
                return request
        abort(404)
        #abort function helps in displaying error messages e.g 404 error.


    @marshal_with(resource_fields)
    def put(self,id):
    #this a put method that modifies data with an id, from request store.
        for request in request_store:
            if(request.id == id):#It takes argument  title, description,category,
                args = reqparse.parse_args()
                request.title = args['title']
                request.description = args['description']
                request.category = args['category']
                return request
        abort(404)


class RequestAll(Resource):
    #this class involves the get all and post methods where get all is a list of previous request and post is a new request which doesn't have an id yet
    @marshal_with(resource_fields)
    def get(self):
        return request_store
    
    
    @marshal_with(resource_fields)
    def post(self):
        args = reqparse.parse_args()
        request = RequestDao( 
                 id= request_store[-1].id +1, #This code shows that from last id request index,you add 1 index position to the new post
                 title = args['title'],
                 description = args['description'],
                 category = args['category'])
        request_store.append(request) #This codes wants to update the request to by including the new post
        return request_store, 201 # 201 message indicates that the request has succeeded and has led to the creation of a resource.

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}       
