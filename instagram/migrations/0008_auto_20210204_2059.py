# Generated by Django 3.1.5 on 2021-02-04 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_auto_20210130_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(3, '길이가...')]),
        ),
    ]