# Generated by Django 2.2.4 on 2019-10-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotdeal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=400)),
                ('time', models.CharField(max_length=100)),
            ],
        ),
    ]
