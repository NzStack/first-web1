# Generated by Django 2.2.16 on 2020-10-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.TextField(max_length=15)),
                ('modelo', models.TextField(max_length=30)),
                ('precio', models.PositiveIntegerField(max_length=8)),
            ],
        ),
    ]
