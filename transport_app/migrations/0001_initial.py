# Generated by Django 3.0.4 on 2020-03-15 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
            ],
        ),
    ]
