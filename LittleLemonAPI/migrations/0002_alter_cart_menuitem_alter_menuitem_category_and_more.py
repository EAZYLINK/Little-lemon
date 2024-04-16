# Generated by Django 5.0.4 on 2024-04-09 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='menuitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonAPI.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LittleLemonAPI.category'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='menuitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittleLemonAPI.menuitem'),
        ),
    ]
