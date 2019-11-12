# Generated by Django 2.2.7 on 2019-11-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('Got_us_throught', models.CharField(choices=[(1, 'SEARCH ENGINE'), (2, 'ADVERTISEMENT'), (3, 'OTHERS'), (0, 'fFEINDS')], default=3, max_length=200)),
                ('new_letter', models.IntegerField(default=0)),
                ('Comment', models.TextField()),
            ],
        ),
    ]