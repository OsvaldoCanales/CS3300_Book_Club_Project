# Generated by Django 4.2.7 on 2023-11-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='title',
            field=models.CharField(default='Default Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='genre',
            field=models.TextField(null=True),
        ),
    ]
