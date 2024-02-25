from django.db import models

class user_model(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class task_model(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(user_model, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    