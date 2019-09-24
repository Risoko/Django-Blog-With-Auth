# Generated by Django 2.2.5 on 2019-09-19 11:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_entries', '0006_auto_20190919_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='entry',
            field=models.TextField(help_text='Your blog entry', validators=[django.core.validators.MinLengthValidator(limit_value=200)], verbose_name='blog entry'),
        ),
    ]