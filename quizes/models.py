from django.db import models
from django.utils.text import slugify
# Create your models here.


class Class(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    class_name = models.CharField(max_length=50, null=True, blank=True)
    teacher_name = models.CharField(max_length=50)
    def __str__(self):
        return self.class_name


class Quiz(models.Model):
    quizzes = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='quizzes')
    id = models.CharField(primary_key=True, max_length=50)
    question_title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question_title

class Condition(models.Model):
    condition = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='condition')
    
    worth = models.CharField(max_length=20, null=True, blank=True)
    hidden = models.BooleanField(default=False)


  
class Variant(models.Model):
    variants = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='variants')
    
    variant_answer = models.CharField(max_length=200, null=True, blank=True)
    right = models.BooleanField(default=True)





