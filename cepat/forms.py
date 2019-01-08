from django import forms
from cepat.models import About, Project, project_images, news, Book, Contact








class AboutForm(forms.ModelForm):
    



    class Meta:
        model = About
        fields = { 'about_title',
                   'about_body', 
                   'mission_title', 
                   'mission_body', 
                   'vision_title', 
                   'vision_body', 
                   'stratergy_title', 
                   'stratergy_body', 
                   }

class GalleryForm(forms.ModelForm):
    



    class Meta:
        model = project_images
        fields = { 'project_image',
                    
                   }

class ProjectForm(forms.ModelForm):
    



    class Meta:
        model = Project
        fields = { 'project_title',
                  'project_detail',
                  'project_summary',
                  'project_results', 
                  'client',
                  'Surface_area',
                  'date_of_finish', 
                  'project_cost',
  
                  'service_surface',
                  'location', 

                   }                   



class NewsForm(forms.ModelForm):
   # content = forms.CharField(widget=forms.Textarea( attrs={"placeholder":"Your message here", "class":"form-control"}))

    class Meta:
        model = news
        fields = [
           
                  'news_title',
                  'news_body',
                  'news_subtitle',
                  'news_image',
                  'author',
                  'clip',
                  
                ]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book

        fields = ('title', 'author', 'pdf')



class ContactForm(forms.ModelForm):
  last_name = forms.CharField( required=True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Last name'}))
  first_name = forms.CharField( max_length=120, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter first Nane'}))
  email = forms.EmailField( max_length=120, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your email'}))
  message = forms.CharField( widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter your message..'}))
 

  class Meta:
      model = Contact

      fields = ('first_name', 'last_name', 'email', 'message')        