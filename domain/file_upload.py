import datetime
from peewee import *
from config.database import connection

class FileUpload(Model):
    id         = AutoField()
    file       = BlobField()
    created_at = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return  self.file

    class Meta:
        database = connection
        table_name = 'file_uploads'