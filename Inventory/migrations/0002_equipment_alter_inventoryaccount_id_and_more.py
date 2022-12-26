# Generated by Django 4.1.4 on 2022-12-26 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('HE', 'Hardware Equipment'), ('UE', 'Usable Equipment')], default='HE', max_length=5)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='inventoryaccount',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inventorytransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='EquipmentAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('AS', 'Assigned'), ('RD', 'Returned')], default='AS', max_length=5)),
                ('assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_equipments', to=settings.AUTH_USER_MODEL)),
                ('assigner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipments_given', to=settings.AUTH_USER_MODEL)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.equipment')),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
    ]