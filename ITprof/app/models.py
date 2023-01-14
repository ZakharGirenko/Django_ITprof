from django.db import models

class HomePageInfo(models.Model):
    title = models.CharField('Заголовок', max_length = 30)
    description = models.TextField('Описание профессии')
    image = models.ImageField('Изображение', upload_to='app/static/images/')
    
    def __str__(self):
        return 'Контент: главная страница'

    class Meta:
        verbose_name = 'Контент: главная страница'
        verbose_name_plural = 'Контент: главная страница'

class RelevancePageInfo(models.Model):

    SalaryByYears_Graph = models.ImageField('График: Динамика уровня зарплат по годам', upload_to='app/static/images/')
    
    SalaryByYears_Table = models.FileField('Таблица: Динамика уровня зарплат по годам(xlsx)', upload_to='app/static/files/', blank=True)

    CountByYears_Graph = models.ImageField('График: Динамика количества вакансий по годам', upload_to='app/static/images/')

    CountByYears_Table = models.FileField('Таблица: Динамика количества вакансий по годам(xlsx)', upload_to='app/static/files/', blank=True)


    def __str__(self):
        return 'Контент: востребованность'

    class Meta:
        verbose_name = 'Контент: востребованность'
        verbose_name_plural = 'Контент: востребованность'




class GeographyPageInfo(models.Model):

    SalaryByCities_Graph = models.ImageField('График: Уровень зарплат по городам', upload_to='app/static/images/', blank=True)
    
    SalaryByCities_Table = models.FileField('Таблица: Уровень зарплат по городам(xlsx)', upload_to='app/static/files/', blank=True)

    CountByCities_Graph = models.ImageField('График: Уровень вакансий по городам', upload_to='app/static/images/', blank=True)

    CountByCities_Table = models.FileField('Таблица: Уровень вакансий по городам(xlsx)', upload_to='app/static/files/', blank=True)
      
    def __str__(self):
        return 'Контент: География'

    class Meta:
        verbose_name = 'Контент: География'
        verbose_name_plural = 'Контент: География'

class SkillsPageInfo(models.Model):

    Skills_Table = models.FileField('Таблица: Навыки(xlsx)', upload_to='app/static/files/', blank=True)
      
    def __str__(self):
        return 'Контент: Навыки'

    class Meta:
        verbose_name = 'Контент: Навыки'
        verbose_name_plural = 'Контент: Навыки'


