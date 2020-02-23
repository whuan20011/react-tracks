# Generated by Django 2.1 on 2020-02-11 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_auto_20200211_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='tracks.Track')),
            ],
        ),
    ]
