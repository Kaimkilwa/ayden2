# Generated by Django 2.2.7 on 2019-11-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayden', '0003_auto_20191112_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='new_letter',
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='got_us_throught',
            field=models.CharField(choices=[(4, ' new latter'), (0, 'FRIENDS'), (2, 'ADVERTISEMENT'), (1, 'SEARCH ENGINE'), (3, 'OTHERS')], default=3, max_length=200),
        ),
    ]
