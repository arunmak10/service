# Generated by Django 4.2.11 on 2024-04-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=50)),
                ('severity', models.CharField(max_length=50)),
                ('deadline', models.DateField()),
            ],
        ),
    ]