from django.contrib import admin
from .models import About,Staff,project_images,Project, news, Book, Contact

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
	list_display = ['about_title',
                   'about_body', 
                   'mission_title', 
                   'mission_body', 
                   'vision_title', 
                   'vision_body', 
                   'stratergy_title', 
                   'stratergy_body', 
                   ]

class StaffAdmin(admin.ModelAdmin):
	list_display = []  

class project_imagesAdmin(admin.ModelAdmin):
	list_display = ['project_image', 'image_name' ] 

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['project_title',
                  'project_detail',
                  'project_summary',
                  'project_results', 
                  'client',
                  'Surface_area',
                  'date_of_finish', 
                  'project_cost',
  
                  'service_surface',
                  'location',
                  ] 



class newsAdmin(admin.ModelAdmin):
      list_display = [ 'news_title',
                      'news_body',
                      'news_subtitle',
                      'news_image',
                      'author',
                      'clip',
                    ] 
admin.site.register(Contact)                    
admin.site.register(news, newsAdmin)                  
admin.site.register(Book)  
admin.site.register(Project)
admin.site.register(project_images, project_imagesAdmin)
admin.site.register(Staff)
admin.site.register(About, AboutAdmin)


