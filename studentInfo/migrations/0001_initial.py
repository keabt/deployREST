# Generated by Django 4.2.7 on 2024-04-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('inTime', models.DateTimeField()),
                ('outTime', models.DateTimeField()),
                ('topics', models.CharField(max_length=100)),
                ('numQuestions', models.IntegerField()),
                ('correctAnswers', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('results', models.IntegerField()),
            ],
        ),
    ]
