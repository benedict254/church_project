# Generated by Django 3.0.2 on 2020-02-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_gallary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]