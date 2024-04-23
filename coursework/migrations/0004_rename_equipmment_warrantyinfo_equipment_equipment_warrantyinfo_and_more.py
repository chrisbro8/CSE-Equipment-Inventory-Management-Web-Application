# Generated by Django 5.0.3 on 2024-04-15 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0003_alter_equipment_equipment_assignedlocation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='Equipmment_warrantyinfo',
            new_name='Equipment_warrantyinfo',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='EquipmentID',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='Booking_alertstatus',
        ),
        migrations.RemoveField(
            model_name='report',
            name='BookingID',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Booking_alertstatus',
        ),
        migrations.RemoveField(
            model_name='report',
            name='User_Dateofbirth',
        ),
        migrations.RemoveField(
            model_name='report',
            name='User_Email',
        ),
        migrations.RemoveField(
            model_name='report',
            name='User_firstname',
        ),
        migrations.RemoveField(
            model_name='report',
            name='User_lastname',
        ),
        migrations.RemoveField(
            model_name='report',
            name='User_phoneNumber',
        ),
        migrations.RemoveField(
            model_name='report',
            name='adminID',
        ),
        migrations.RemoveField(
            model_name='report',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='User_Dateofbirth',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='User_Email',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='User_firstname',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='User_lastname',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='admin_address',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='admin_phoneNumber',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='adminID',
        ),
        migrations.AddField(
            model_name='admin',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.user'),
        ),
        migrations.AddField(
            model_name='adminandequipment',
            name='Admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.admin'),
        ),
        migrations.AddField(
            model_name='adminandequipment',
            name='Equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.equipment'),
        ),
        migrations.AddField(
            model_name='report',
            name='Admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.admin'),
        ),
        migrations.AddField(
            model_name='report',
            name='Equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.equipment'),
        ),
        migrations.AddField(
            model_name='report',
            name='Reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.reservation'),
        ),
        migrations.AddField(
            model_name='report',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.user'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.admin'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursework.user'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_phoneNumber',
            field=models.IntegerField(null=True),
        ),
    ]
