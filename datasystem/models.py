from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Lecturer(models.Model):
    name = models.CharField(max_length=64,)
    number = models.IntegerField()
    def __str__(self):
        return f"{self.name}"

class Schedules(models.Model):
    classID = models.CharField(max_length=64)
    dayOfWeek = models.IntegerField()
    group = models.CharField(max_length=3)
    courseID = models.CharField(max_length=64)
    lectureID = models.IntegerField()
    period = models.CharField(max_length=64)
    className = models.CharField(max_length=64)
    credit = models.IntegerField()
    auditorium = models.CharField(max_length=64)
    maxAMount = models.IntegerField()
    def __str__(self):
        return f"{self.classID}"
class Enrolllist(models.Model):
    studentID =models.CharField(max_length=64)
    classID = models.CharField(max_length=64)
    group = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.studentID+self.classID}"
class examschedule(models.Model):
    time = models.CharField(max_length=64)
    dayOfWeek = models.IntegerField()
    date = models.CharField(max_length=64)
    classID = models.CharField(max_length=64)
    className = models.CharField(max_length=64)
    credit = models.IntegerField()
    lectureName = models.CharField(max_length=64)
    amount = models.IntegerField()
    numberOfRoom = models.IntegerField()
    CT = models.IntegerField()
    auditorium =  models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.classID}"