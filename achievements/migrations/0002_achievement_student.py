# Generated by Django 3.2 on 2021-08-27 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='student',
            field=models.ForeignKey(blank=True, help_text='Student(s) Achievements', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_achievements', to='account.student'),
        ),
    ]
