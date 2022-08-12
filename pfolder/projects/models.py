from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  Projects(models.Model):
    project_owner=models.ForeignKey(User,on_delete=models.CASCADE)
    project_name=models.CharField(max_length=500)
    project_files=models.FileField(upload_to="static/files/")
    def __str__(self) -> str:
        return  self.project_name
