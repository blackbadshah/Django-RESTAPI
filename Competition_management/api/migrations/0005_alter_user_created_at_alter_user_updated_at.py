# Generated by Django 4.1.6 on 2023-02-14 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_competition_id_alter_entry_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
