# Generated by Django 2.2.5 on 2019-09-17 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 14, 49, 8, 370338, tzinfo=utc), help_text='Enter the publication date of the article.', verbose_name='publish date'),
        ),
    ]
