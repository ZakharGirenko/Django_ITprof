# Generated by Django 4.1.5 on 2023-01-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_relevancepageinfo_salarybyyears_16_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_16',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_17',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_18',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_19',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_20',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_21',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_22',
        ),
        migrations.RemoveField(
            model_name='relevancepageinfo',
            name='CountByYears_23',
        ),
        migrations.AddField(
            model_name='relevancepageinfo',
            name='CountByYears_Table',
            field=models.FileField(blank=True, upload_to='app/static/files/', verbose_name='Таблица: Динамика количества вакансий по годам(xlsx)'),
        ),
        migrations.AlterField(
            model_name='relevancepageinfo',
            name='SalaryByYears_Table',
            field=models.FileField(blank=True, upload_to='app/static/files/', verbose_name='Таблица: Динамика уровня зарплат по годам(xlsx)'),
        ),
    ]
