# Generated by Django 4.1.1 on 2022-09-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bib_graphql', '0003_book_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
    ]
