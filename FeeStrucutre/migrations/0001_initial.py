# Generated by Django 2.0.4 on 2018-05-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TUTION_FEE', models.PositiveIntegerField()),
                ('EXAM_FEE', models.PositiveIntegerField()),
                ('HOSTEL_FEE', models.PositiveIntegerField()),
                ('BUS_FEE', models.PositiveIntegerField()),
                ('EXTRA_FEE', models.PositiveIntegerField()),
            ],
        ),
    ]
