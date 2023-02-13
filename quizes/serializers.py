from rest_framework import serializers
from .models import *



class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id','variant_name', 'variant_answer', 'right']

class QuizSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id','question_number', 'question_title', 'hidden']
class ClassSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = Class
        fields = ['id','class_name', 'teacher_name']