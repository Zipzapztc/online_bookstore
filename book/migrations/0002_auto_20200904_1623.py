# Generated by Django 2.2.13 on 2020-09-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]