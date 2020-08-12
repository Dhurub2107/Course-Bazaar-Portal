# Generated by Django 2.0.4 on 2018-05-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COLLEGENAME', models.CharField(max_length=20)),
                ('COMPANYNAME', models.CharField(max_length=150)),
                ('COURSE', models.CharField(max_length=25)),
                ('NOOFPERSON', models.IntegerField()),
                ('PACKAGE', models.PositiveIntegerField()),
                ('LOCATION', models.CharField(max_length=20)),
            ],
        ),
    ]