# Generated by Django 2.2.28 on 2023-07-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_site', '0004_auto_20230719_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='purpose',
            field=models.TextField(help_text='Enter a brief description', max_length=200),
        ),
    ]