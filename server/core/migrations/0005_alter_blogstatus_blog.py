# Generated by Django 3.2 on 2022-07-29 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220728_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogstatus',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='core.blog'),
        ),
    ]
