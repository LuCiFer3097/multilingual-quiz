from django.db import models

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    questionText = models.CharField(max_length=100)
    lanuguage = models.CharField(max_length=100)

    def __str__(self):
        return self.questionText


class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    choice = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice
