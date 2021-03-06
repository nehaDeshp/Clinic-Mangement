# Generated by Django 2.0.2 on 2018-02-11 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=5)),
                ('test_date', models.DateTimeField()),
                ('test_details', models.TextField()),
                ('result_status', models.CharField(max_length=10)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='laboratory',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.Patient'),
        ),
    ]
