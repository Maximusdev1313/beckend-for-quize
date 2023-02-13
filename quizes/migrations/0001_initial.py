# Generated by Django 4.1.6 on 2023-02-13 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(blank=True, max_length=50, null=True)),
                ('teacher_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.CharField(blank=True, max_length=10, null=True)),
                ('question_title', models.CharField(blank=True, max_length=200, null=True)),
                ('hidden', models.BooleanField(default=True)),
                ('quizzes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='quizes.class')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_name', models.CharField(blank=True, max_length=10, null=True)),
                ('variant_answer', models.CharField(blank=True, max_length=200, null=True)),
                ('right', models.BooleanField(default=True)),
                ('variants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='quizes.quiz')),
            ],
        ),
    ]