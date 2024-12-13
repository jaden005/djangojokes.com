# Generated by Django 5.1.4 on 2024-12-13 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0007_joke_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='jokes', to='jokes.category'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='JokeVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jokevotes', to='jokes.joke')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jokevotes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('user', 'joke'), name='one_vote_per_user_per_joke')],
            },
        ),
    ]