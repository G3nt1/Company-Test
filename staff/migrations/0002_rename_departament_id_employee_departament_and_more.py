# Generated by Django 4.1 on 2022-09-09 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='departament_id',
            new_name='departament',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emegency_id',
            new_name='emegency',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='supervisor_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.details'),
        ),
        migrations.AddField(
            model_name='employee',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.employee'),
        ),
    ]
