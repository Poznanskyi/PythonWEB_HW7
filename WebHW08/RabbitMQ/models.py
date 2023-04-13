from mongoengine import *

connect(host="mongodb+srv://poz:2RbN342PoZ@firstcluster.dxzj24g.mongodb.net/?retryWrites=true&w=majority")


class Contacts(Document):
    fullname = StringField(max_length=80, required=True)
    email = StringField(max_length=50)
    number = StringField(max_length=50)
    send = BooleanField(default=False)