# Generated by Django 3.0.3 on 2020-05-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200528_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writenotes',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
