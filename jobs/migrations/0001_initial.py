# Generated by Django 5.1.4 on 2024-12-06 18:08

import django.core.validators
import django.db.models.deletion
import jobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text='A valid email address.', max_length=254)),
                ('website', models.URLField(blank=True, validators=[django.core.validators.URLValidator(schemes=['http', 'https'])])),
                ('employment_type', models.CharField(choices=[(None, '--Please choose--'), ('ft', 'Full-time'), ('pt', 'Part-time'), ('contract', 'Contract work')], max_length=10)),
                ('start_date', models.DateField(help_text='The earliest date you can start working.', validators=[jobs.models.validate_future_date])),
                ('available_days', models.CharField(max_length=20)),
                ('desired_hourly_wage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cover_letter', models.TextField()),
                ('confirmation', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]