# Generated by Django 4.1 on 2022-09-09 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_rename_departament_id_employee_departament_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='details',
        ),
        migrations.AddField(
            model_name='employee',
            name='adress',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Details',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emegency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.emergencycontact'),
        ),
        migrations.DeleteModel(
            name='Emergency',
        ),
    ]
