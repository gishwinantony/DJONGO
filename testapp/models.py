from djongo import  models

class Urls(models.Model):
    _id = models.ObjectIdField()
    client_url=models.CharField(max_length=500)
    mapped_key=models.CharField(max_length=500)
