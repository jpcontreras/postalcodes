from config.database import connection

class FileUpload(Model):
    id        = AutoField()
    file      = BlobField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return  self.file

    class Meta:
        database = connection
        table_name = 'file_uploads'