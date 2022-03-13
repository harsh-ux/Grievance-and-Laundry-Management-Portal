# Generated by Django 3.2.9 on 2022-03-13 15:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_hostel_name'),
        ('laundry', '0003_rename_pent_blaundry_pant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('complaint_pic', models.ImageField(upload_to=None)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hostel', models.CharField(choices=[('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B5'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('I2', 'I2')], default='B1', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.studentprofile')),
            ],
        ),
    ]