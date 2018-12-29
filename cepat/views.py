from django.shortcuts import render, redirect, get_object_or_404, reverse


from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse,HttpRequest, HttpResponseRedirect

def book_list(request):
    
    return render(request, 'cepat/book_list.html')

def upload_book(request):
    
    return render(request, 'cepat/upload_book.html')

def  home(request):

     
      return render(request, "cepat/index.html") 







def aboutView(request):
    




    return render(request, 'cepat/about.html')    
     
       



def  service(request):
     
     return render(request, "cepat/service.html")


def  agriculture(request):
     
     return render(request, "cepat/agriculture.html")


def  energy(request):
     
     return render(request, "cepat/energy.html")


def  report(request):
    
     
     return render(request, "cepat/report.html")

def  report_detail(request):
     
     
      return render(request, "cepat/report.html")


     
     





def project(request):
   


    return render(request, 'cepat/project.html')
     
def project_detail(request):
    
    return render(request, "cepat/project-detail.html")





def  resource(request):
     
     return render(request, "cepat/resource.html")

def  enquire(request):
     
     return render(request, "cepat/enquire.html")

       



def gallery(request):
    




    return render(request, "cepat/gallery.html")    
     
      

def  contact(request):

    

    return render(request, "cepat/contact.html")
     
                










def news_detail(request):
    
    return render(request, "cepat/news_detail.html")


     
     


def news_list(request):
   



  

    return render(request, "cepat/news.html")





def  history(request):
    

  
     
    return render(request, "cepat/history.html")





def management(request):
   

 
     
    return render(request, "cepat/management.html")
     
     

def  clients(request):
    

  
     
    return render(request, "cepat/clients.html")
     
    

def  investors(request):
     
     return render(request, "cepat/investors.html")

def  team(request):
     
     return render(request, "cepat/team.html")

def  objectives(request):
     
     return render(request, "cepat/objectives.html")




    
