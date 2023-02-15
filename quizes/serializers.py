from rest_framework import serializers
from .models import *



class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'variant_answer', 'right','variants']
class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ['id', 'worth', 'hidden', 'condition']
class QuizSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)
    condition = ConditionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'question_title', 'quizzes', 'condition', 'variants']

class ClassSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = Class
        fields = ['id','class_name', 'teacher_name', 'quizzes']