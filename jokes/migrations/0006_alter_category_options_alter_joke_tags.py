# Generated by Django 5.1.4 on 2024-12-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0005_tag_alter_category_options_joke_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, to='jokes.tag'),
        ),
    ]
