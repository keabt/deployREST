from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    inTime = models.DateTimeField()
    outTime = models.DateTimeField()
    topics = models.CharField(max_length=100)
    numQuestions = models.IntegerField()
    correctAnswers = models.IntegerField()
    difficulty = models.IntegerField()
    results = models.IntegerField()