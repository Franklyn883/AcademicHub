# Generated by Django 5.0.6 on 2024-05-24 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_department_faculty_departmenthead_and_more'),
        ('student', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department'),
        ),
    ]