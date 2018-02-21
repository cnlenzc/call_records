# Generated by Django 2.0.2 on 2018-02-21 21:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrecord',
            name='destination',
            field=models.CharField(help_text='The subscriber phone number that originated the call', max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'AAXXXXXXXXX'.Where AA is the area code and XXXXXXXXX is the phone number.", regex='^\\d{10,11}$')]),
        ),
        migrations.AlterField(
            model_name='callrecord',
            name='source',
            field=models.CharField(help_text='The subscriber phone number that originated the call', max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: 'AAXXXXXXXXX'.Where AA is the area code and XXXXXXXXX is the phone number.", regex='^\\d{10,11}$')]),
        ),
    ]