# Generated by Django 3.0.2 on 2020-03-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=12)),
                ('classes', models.TextField(default='', max_length=120)),
            ],
        ),
    ]