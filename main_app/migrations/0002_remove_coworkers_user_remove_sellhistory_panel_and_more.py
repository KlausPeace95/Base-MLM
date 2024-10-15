# Generated by Django 4.1.7 on 2023-02-17 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coworkers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sellhistory',
            name='panel',
        ),
        migrations.AddField(
            model_name='coworkers',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.level'),
            preserve_default=False,
        ),
    ]