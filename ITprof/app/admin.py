from django.contrib import admin
import app.models 

admin.site.register(app.models.HomePageInfo)
admin.site.register(app.models.RelevancePageInfo)
admin.site.register(app.models.GeographyPageInfo)
admin.site.register(app.models.SkillsPageInfo)
