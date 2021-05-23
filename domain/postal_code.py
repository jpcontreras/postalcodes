from config.database import connection

class PostalCode(Model):
    id        = AutoField()
    latitude      = DoubleField()
    longitude = DoubleField()
    postal_details = JSONField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return  self.postal_details

    class Meta:
        database = connection
        table_name = 'file_uploads'