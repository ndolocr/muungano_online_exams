# Generated by Django 4.2.13 on 2024-08-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('examination_paper', '0001_initial'),
        ('image', '0001_initial'),
        ('subject', '0001_initial'),
        ('passage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('marks', models.IntegerField()),
                ('question_number', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('examination_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination_paper.examinationpaper')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='image.image')),
                ('passage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='passage.passage')),
                ('subjects', models.ManyToManyField(to='subject.subject')),
                ('tags', models.ManyToManyField(to='tags.tag')),
            ],
        ),
    ]