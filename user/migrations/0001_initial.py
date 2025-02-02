# Generated by Django 4.2.3 on 2024-07-05 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaqt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Polyabron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismfamilya', models.CharField(max_length=200)),
                ('jamo1', models.CharField(max_length=1000)),
                ('jamo2', models.CharField(max_length=1000)),
                ('kun', models.DateField()),
                ('tel_raqam', models.IntegerField()),
                ('tel_raqam2', models.IntegerField()),
                ('izoh', models.TextField()),
                ('vaqti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.vaqt')),
            ],
        ),
    ]
