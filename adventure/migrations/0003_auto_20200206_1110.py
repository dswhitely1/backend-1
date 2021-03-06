# Generated by Django 3.0.3 on 2020-02-06 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200204_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT ITEM', max_length=50)),
                ('description', models.TextField(default='DEFAULT DESCRIPTION', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RoomItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Item')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='items',
            field=models.ManyToManyField(through='adventure.Inventory', to='adventure.Item'),
        ),
        migrations.AddField(
            model_name='room',
            name='items',
            field=models.ManyToManyField(through='adventure.RoomItem', to='adventure.Item'),
        ),
    ]
