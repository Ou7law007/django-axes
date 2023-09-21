# Generated by Django 4.2.4 on 2023-09-21 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('axes', '0008_accessfailurelog'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesslog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
