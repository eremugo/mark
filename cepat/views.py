from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import About, Project, project_images, news, Book, Contact
from .forms import AboutForm, ProjectForm,GalleryForm, NewsForm, BookForm, ContactForm
from django.views.generic import TemplateView,DetailView, ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse,HttpRequest, HttpResponseRedirect

def book_list(request):
    books = Book.objects.all()
    return render(request, 'cepat/book_list.html', { 'books': books })

def upload_book(request):
    if request == 'POST':
       form = BookForm(request.POST, request.FILES)
       if form.is_valid():
          form.save()
          return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'cepat/upload_book.html', {'form': form})

def  home(request):

      queryset = About.objects
      context={

          "Object_list": queryset
             }
     
      return render(request, "cepat/index.html", context) 







class aboutView(TemplateView):
    template_name='cepat/about.html'



    def get(self, request):
        form = AboutForm()
        abouts = About.objects.all()
        
        
        

        args = { 'form':form, 'abouts': abouts }

        return render(request, self.template_name, args)    
     
       



def  service(request):
     
     return render(request, "cepat/service.html")


def  agriculture(request):
     
     return render(request, "cepat/agriculture.html")


def  energy(request):
     
     return render(request, "cepat/energy.html")


def  report(request):
     books = Book.objects.all()
     
     return render(request, "cepat/report.html", { 'books': books })

def  report_detail(request):
      if request == 'POST':
          form = BookForm(request.POST, request.FILES)
          if form.is_valid():
             form.save()
             return redirect('book_list')
      else:
          form = BookForm()
     
      return render(request, "cepat/report.html", {'form': form})


     
     





class project(TemplateView):
    template_name='cepat/project.html'



    def get(self, request):
        form = ProjectForm()
        projects = Project.objects.all()
        
        
        

        args = { 'form':form, 'projects': projects }

        return render(request, self.template_name, args) 
     
class project_detail(DetailView):
    template_name = 'cepat/project-detail.html'
    queryset = Project.objects.all()


    def get_object(self):
      print(self.kwargs)
      pk = self.kwargs.get("pk")
      project = get_object_or_404(Project, pk=pk)
      return project


#def  project_detail(request, id):
     #project = Project.objects.get(id=id)
     #context = {'project': project}
     
     #return render(request, "cepat/project-detail.html", context) 


def  resource(request):
     
     return render(request, "cepat/resource.html")

def  enquire(request):
     
     return render(request, "cepat/enquire.html")

       



class gallery(TemplateView):
    template_name="cepat/gallery.html"



    def get(self, request):
        form = GalleryForm()
        gallery = project_images.objects.all()
        
        
        

        args = { 'form':form, 'gallery': gallery }

        return render(request, self.template_name, args)    
     
      

def  contact(request):

    template = "cepat/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, template, context)
     
                










class news_detail(DetailView):
    template_name = "cepat/news-detail.html"
    queryset = news.objects.all()


    def get_object(self):
      print(self.kwargs)
      pk = self.kwargs.get("pk")
      nan = get_object_or_404(news, pk=pk)
      return nan


     
     


class news_list(TemplateView):
    template_name="cepat/news.html"



    def get(self, request):
        news_form = NewsForm()
        nans = news.objects.all()
        
        
        

        args = { 'news_form':news_form, 'nans': nans }

        return render(request, self.template_name, args)





def  history(request):
    template = "cepat/history.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    context = {
        "form": form,
    }
     
    return render(request, template, context)





def management(request):
    template = "cepat/management.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    context = {
        "form": form,
    }
     
    return render(request, template, context)
     
     

def  clients(request):
    template = "cepat/clients.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    context = {
        "form": form,
    }
     
    return render(request, template, context)
     
    

def  investors(request):
     
     return render(request, "cepat/investors.html")

def  team(request):
     
     return render(request, "cepat/team.html")

def  objectives(request):
     
     return render(request, "cepat/objectives.html")



#class news_list(ListView):
    #template_name = "cepat/news.html"
   # queryset = tweet.objects.all()

    #def get_queryset(self, *args, **kwargs):
        #qs = news.objects.all()
       # print(self.request.GET)
        #query = self.request.GET.get("q", None)
        #if query is not None:
            #qs = qs.filter( Q(content__icontains=query))

            #return qs



    #def get_context_data(self, *args, **kwargs):
       # context = super(news_list, self).get_context_data(*args, **kwargs)
        #context["create_form"] = newsForm
        #context["create_url"]= reverse_lazy("cepat:home")
        #print(context)
       # return context      
     
    