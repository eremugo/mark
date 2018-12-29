from django.urls import path
from .import views


app_name = "cepat"

urlpatterns = [
     path('', views.home, name='home' ),
     path('about/', views.aboutView, name='about' ),
     path('service/', views.service, name='service' ),
     path('agriculture/', views.agriculture, name='agriculture' ),
     path('energy/', views.energy, name='energy' ),
     path('report/', views.report, name='report' ),
     path('report_detail/', views.report_detail, name='report_detail' ),

     path('book_list/', views.book_list, name='book_list' ),
     path('upload_book/', views.upload_book, name='upload_book' ),


     path('project/',  views.project, name='project' ),
     path('cepat/project-detail/<int:pk>/', views.project_detail, name='project-detail' ),
     path('resource/', views.resource, name='resource' ),
     path('enquire/', views.enquire, name='enquire' ),
     path('news/', views.news_list, name='news' ),
     path('cepat/news-detail/<int:pk>/', views.news_detail, name='news-detail' ),
     path('gallery/', views.gallery, name='gallery' ),
     path('contact/', views.contact, name='contact' ),

     path('history/', views.history, name='history' ),

     path('objectives/', views.objectives, name='objectives' ),
     path('team/', views.team, name='team' ),
    
     path('management/', views.management, name='management' ),
     path('investors/', views.investors, name='investors' ),
     path('clients/', views.clients, name='clients' ),
]