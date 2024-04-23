# Generated by Django 5.0.3 on 2024-04-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=50, null=True)),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('Dateofbirth', models.DateField(auto_now_add=True, null=True)),
                ('RoleType', models.CharField(max_length=50, null=True)),
                ('accountstatus', models.IntegerField(null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('currentReservation', models.CharField(max_length=50, null=True)),
                ('historicalreservation', models.CharField(max_length=50, null=True)),
                ('phoneNumber', models.IntegerField(verbose_name='')),
                ('address', models.CharField(max_length=50, null=True)),
                ('adminID', models.CharField(max_length=50, null=True)),
                ('userType', models.IntegerField(null=True)),
            ],
        ),
    ]
