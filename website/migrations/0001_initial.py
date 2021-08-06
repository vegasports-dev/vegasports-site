# Generated by Django 3.2.6 on 2021-08-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bookkeepername', models.CharField(max_length=30)),
                ('states', models.TextField()),
                ('wlecomeoffer', models.TextField()),
                ('vsnotes', models.TextField()),
                ('vsrank', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('wlecomeofferrank', models.IntegerField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=30)),
                ('sportsbooks', models.TextField()),
            ],
        ),
    ]