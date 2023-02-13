from django.db import models
from django.utils.text import slugify
# Create your models here.


class Class(models.Model):
    class_name = models.CharField(max_length=50, null=True, blank=True)
    teacher_name = models.CharField(max_length=50)
    def __str__(self):
        return self.class_name

class Quiz(models.Model):
    quizzes = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='quizzes')

    question_number = models.CharField(max_length=10, null=True, blank=True)
    question_title = models.CharField(max_length=200, null=True, blank=True)
    hidden = models.BooleanField(default=True)

    def __str__(self):
        return self.question_title

class Variant(models.Model):
    variants = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='variants')
    
    variant_name = models.CharField(max_length=10, null=True, blank=True)
    variant_answer = models.CharField(max_length=200, null=True, blank=True)
    right = models.BooleanField(default=True)





