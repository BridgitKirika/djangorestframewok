# Generated by Django 4.0.5 on 2022-06-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wepapp', '0002_rename_first_name_employees_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
