# Generated by Django 4.2.13 on 2024-08-31 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logs', '0001_initial'),
        ('examination_body', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinationbodylogs',
            name='action_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs_on_action_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examinationbodylogs',
            name='examination_body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs_on_examination_body', to='examination_body.examinationbody'),
        ),
    ]
