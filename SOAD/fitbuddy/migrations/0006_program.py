# Generated by Django 3.1.2 on 2020-10-31 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitbuddy', '0005_auto_20201031_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('WL', 'Weightloss'), ('WG', 'WG'), ('AB', 'AB'), ('RG', 'RG')], default='RG', max_length=2)),
                ('number_of_sessions', models.IntegerField()),
                ('hours_per_session', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('fcenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitbuddy.fitnesscenter')),
            ],
        ),
    ]
