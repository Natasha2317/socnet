# Generated by Django 3.1.4 on 2021-01-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], default='male', max_length=6),
        ),
    ]