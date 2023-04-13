from mongoengine import *

connect(host="mongodb+srv://poz:2RbN342PoZ@firstcluster.dxzj24g.mongodb.net/?retryWrites=true&w=majority")


class Authors(Document):
    fullname = StringField(max_length=100, required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
    meta = {"allow_inheritance": True}