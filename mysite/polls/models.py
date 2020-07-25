import datetime 

from django.db import models
from django.utils import timezone 

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Inherit model/s from Django 
#ForeignKey = connected to a question, which is a class 
#Cascade = if you delete question, you delete all cho0ices attached to that question 
#CharField = character field (text) 

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    

