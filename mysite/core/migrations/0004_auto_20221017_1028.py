# Generated by Django 3.2.16 on 2022-10-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_currentuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentuser',
            name='createdDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='currentuser',
            name='last_login',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='currentuser',
            name='updatedDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
