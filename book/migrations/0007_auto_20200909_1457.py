# Generated by Django 2.2.13 on 2020-09-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(upload_to='books/%Y/%m/%d'),
        ),
    ]
