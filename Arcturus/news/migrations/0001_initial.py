# Generated by Django 3.2 on 2023-05-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('id_field', models.IntegerField(verbose_name='id')),
            ],
        ),
    ]
