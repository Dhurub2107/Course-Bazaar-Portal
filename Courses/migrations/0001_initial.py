# Generated by Django 2.0.4 on 2018-05-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COURSE',
            fields=[
                ('COURSES', models.CharField(choices=[('BCA', 'BCA'), ('MCA', 'MCA'), ('B.TECH', 'B.TECH'), ('PHD', 'PHD'), ('MBA', 'MBA'), ('BBA', 'BBA')], default='OTHERS', max_length=20)),
                ('POSTEDBY', models.CharField(choices=[('admin', 'ADMIN'), ('college', 'COLLEGE')], max_length=150)),
                ('COLLEGE_NAME', models.CharField(choices=[('TMU', 'TEERTHANKER MAHAVEER UNIVERSITY'), ('AKG', 'AJY KUMAR GARG'), ('MJPRU', 'MJPRU'), ('ABES', 'ABES')], max_length=25)),
                ('CI', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('LOCATION', models.CharField(choices=[('PAAKWADA', 'PAAKWADA'), ('LOHIA NAGAR', 'LOHIA NAGAR'), ('NEW BUSSTAND', 'NEW BUSSTAND')], max_length=50)),
                ('MINIMUM_QUCALIFICATION', models.CharField(choices=[('10+2', '10+2'), ('UG', 'UG'), ('PG', 'PG')], max_length=20)),
                ('ELEGIBILITY', models.CharField(max_length=20)),
                ('FEES_RANGE', models.CharField(choices=[('2L-3L', '2L-3L'), ('3L-4L', '3L-4L'), ('4L-5L', '4L-5L'), ('5L<', '5L<')], max_length=50)),
                ('CONTACT_PERSON', models.CharField(max_length=20)),
                ('CONTACT_PERSON_MOBILE', models.IntegerField()),
                ('COLLEGE_WEBSITE', models.URLField(max_length=50)),
                ('PLACEMENT', models.CharField(choices=[('50-60', '50-60%'), ('60-70', '60-70%'), ('70-80', '70-80%'), ('80-90', '80-90%'), ('90-100', '90-100%')], max_length=20)),
                ('LASTDATE', models.DateField()),
                ('CURRENTSTATUS', models.CharField(max_length=50)),
            ],
        ),
    ]