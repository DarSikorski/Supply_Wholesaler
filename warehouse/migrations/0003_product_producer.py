# Generated by Django 3.2.9 on 2022-01-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20220118_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
