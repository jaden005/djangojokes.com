# Generated by Django 5.1.4 on 2024-12-12 21:11

import djangojokes.storage_backends
import jobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', storage=djangojokes.storage_backends.PrivateMediaStorage(), upload_to='resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]
