# Generated by Django 2.2.7 on 2019-11-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayden', '0004_auto_20191112_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='got_us_throught',
            field=models.CharField(choices=[(4, 'news letter'), (1, 'SEARCH ENGINE'), (0, 'FRIENDS'), (2, 'ADVERTISEMENT'), (3, 'OTHERS')], default=3, max_length=200),
        ),
    ]
