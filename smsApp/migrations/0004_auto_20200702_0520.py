# Generated by Django 3.0.7 on 2020-07-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0003_auto_20200701_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipent',
            name='id',
        ),
        migrations.AlterField(
            model_name='receipent',
            name='userID',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]