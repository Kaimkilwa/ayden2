# Generated by Django 2.2.7 on 2019-11-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayden', '0005_auto_20191112_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='got_us_throught',
            field=models.CharField(choices=[(2, 'ADVERTISEMENT'), (1, 'SEARCH ENGINE'), (4, 'NEWS LETTER'), (0, 'FRIENDS'), (3, 'OTHERS')], default=3, max_length=200),
        ),
    ]