# Generated by Django 3.2.4 on 2021-09-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private', '0002_auto_20210810_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcard',
            name='back',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vcard',
            name='front',
            field=models.CharField(max_length=50),
        ),
    ]
