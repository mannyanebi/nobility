# Generated by Django 3.2 on 2021-08-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the Achievement', max_length=256, null=True)),
                ('type', models.CharField(choices=[('High CGPA', 'High CGPA'), ('Leadership Position', 'Leadership Position'), ('Academic Scholarship', 'Academic Scholarship'), ('Extra-curricular Activities', 'Extra-curricular Activities')], help_text='Type of Achievement', max_length=60)),
                ('year', models.DateField(help_text='Date of Achievement', null=True)),
            ],
        ),
    ]
