# Generated by Django 3.2.12 on 2022-07-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]