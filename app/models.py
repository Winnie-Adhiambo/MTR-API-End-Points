

# this is where your models go
request_store={}


# class user
class User():
    def __init__(self,username,password,confirmpassword):
        self.username=username
        self.password=password
        self.confirmpassword=confirmpassword


# class requests
class Request(User):
    
    count=1
    def __init__(self,title,type,date):
        
        self.title=title
        self.type=type
        self.date=date
        self.id = Request.count
        Request.count +=1

    def add_request(self):
        request_store[self.id]=[self.title,self.type,self.date]
        return request_store

