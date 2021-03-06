# Generated by Django 2.0.4 on 2018-05-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('ID', models.CharField(choices=[('cd01', 'CD01'), ('cd02', 'CD02'), ('cd03', 'CD03'), ('cd04', 'CD04'), ('cd05', 'CD05'), ('cd06', 'CD06'), ('cd07', 'CD07'), ('cd08', 'CD08'), ('cd09', 'CD09'), ('cd10', 'CD10')], max_length=10, primary_key=True, serialize=False)),
                ('CONSULTANT_NAME', models.CharField(default='XYZ', max_length=20)),
                ('COUNTRY', models.CharField(choices=[('INDIA', 'INDIA'), ('US', 'US'), ('DUBAI', 'DUBAI'), ('SRI LANKA', 'SRI LANKA'), ('Bangladesh', 'Bangladesh')], max_length=25)),
                ('STATE', models.CharField(choices=[('UP', 'UP'), ('MP', 'MP'), ('TAMIL_NAADU', 'TAMIL_NADDU'), ('DELHI', 'DELHI'), ('OTHERS', 'OTHERS')], max_length=20)),
                ('CITY', models.CharField(choices=[('MORADABAD', 'MORADABAD'), ('GHAZIABAD', 'GHAZIABAD'), ('MUMBAI', 'MUMBAI'), ('CHENNAI', 'CHENNAI'), ('DELHI', 'DELHI'), ('WASHINGTON', 'WASHINGTON'), ('OTHERS', 'OTHERS')], max_length=20)),
                ('PINCODE', models.PositiveIntegerField()),
                ('MAIL_ID', models.EmailField(max_length=254)),
                ('MOBILE1', models.PositiveIntegerField()),
                ('MOBILE2', models.PositiveIntegerField()),
            ],
        ),
    ]
