# Generated by Django 3.2.18 on 2023-03-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20230322_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
