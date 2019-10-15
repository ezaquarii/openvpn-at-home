# Generated by Django 2.2.4 on 2019-10-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_blocklisturl_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='config_file_extension',
            field=models.CharField(choices=[('ovpn', 'OVPN'), ('conf', 'CONF')], default='ovpn', max_length=10),
        ),
    ]
