# Generated by Django 4.2.7 on 2023-11-05 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_catalog_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='Catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_app.catalog'),
        ),
    ]
