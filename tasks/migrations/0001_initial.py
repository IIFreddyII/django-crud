# Generated by Django 4.2.9 on 2024-01-19 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('random_slug', models.SlugField(editable=False, max_length=8, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
                ('due_date', models.DateField()),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
