# Generated by Django 4.1.6 on 2023-02-13 07:15

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(limit_value=3)])),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
