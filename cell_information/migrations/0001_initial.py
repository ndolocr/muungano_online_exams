# Generated by Django 4.2.13 on 2024-08-31 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_x', models.IntegerField()),
                ('cell_y', models.IntegerField()),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.table')),
            ],
            options={
                'db_table': 'cell_information',
            },
        ),
    ]
