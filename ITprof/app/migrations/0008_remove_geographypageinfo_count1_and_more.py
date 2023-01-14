# Generated by Django 4.1.5 on 2023-01-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_relevancepageinfo_countbyyears_16_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Count1',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Count2',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Count3',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Count4',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Count5',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='CountGraph',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Salary1',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Salary2',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Salary3',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Salary4',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='Salary5',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='SalaryGraph',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='city1',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='city2',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='city3',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='city4',
        ),
        migrations.RemoveField(
            model_name='geographypageinfo',
            name='city5',
        ),
        migrations.AddField(
            model_name='geographypageinfo',
            name='CountByYears_Graph',
            field=models.ImageField(blank=True, upload_to='app/static/images/', verbose_name='График: Уровень вакансий по городам'),
        ),
        migrations.AddField(
            model_name='geographypageinfo',
            name='CountByYears_Table',
            field=models.FileField(blank=True, upload_to='app/static/files/', verbose_name='Таблица: Уровень вакансий по городам(xlsx)'),
        ),
        migrations.AddField(
            model_name='geographypageinfo',
            name='SalaryByYears_Graph',
            field=models.ImageField(blank=True, upload_to='app/static/images/', verbose_name='График: Уровень зарплат по городам'),
        ),
        migrations.AddField(
            model_name='geographypageinfo',
            name='SalaryByYears_Table',
            field=models.FileField(blank=True, upload_to='app/static/files/', verbose_name='Таблица: Уровень зарплат по городам(xlsx)'),
        ),
    ]
