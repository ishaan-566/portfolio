# Generated by Django 3.2.4 on 2021-08-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
