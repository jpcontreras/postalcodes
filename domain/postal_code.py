import datetime
from peewee import *
from config.database import connection

class PostalCode(Model):
    id             = AutoField()
    latitude       = DoubleField()
    longitude      = DoubleField()
    postal_details = CharField() #I had problems with JSONField and BinaryJSONField - NameError: name 'BinaryJSONField' is not defined
    created_at     = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return  self.postal_details

    class Meta:
        database = connection
        table_name = 'postal_codes'

PostalCode.create_table()