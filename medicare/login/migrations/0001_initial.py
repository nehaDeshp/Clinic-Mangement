# Generated by Django 2.0.2 on 2018-02-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
            ],
        ),
    ]