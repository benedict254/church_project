# Generated by Django 3.0.2 on 2020-02-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_login_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]
