from django.db import models


# Create your models here.
class Staff(models.Model):
    staff_image = models.ImageField(upload_to='staff_image', blank=True)
    staff_name = models.CharField(max_length=100, default='',  blank=True)
    staff_detail = models.TextField(blank=True)
    staff_title = models.CharField(max_length=100, default='',  blank=True) 

class About(models.Model):
   about_title = models.CharField(max_length=100, default='',  blank=True)
   about_body = models.TextField(blank=True)
   mission_title = models.CharField(max_length=100, default='',  blank=True)
   mission_body = models.TextField(blank=True)
   vision_title = models.CharField(max_length=100, default='',  blank=True)
   vision_body = models.TextField(blank=True)
   stratergy_title = models.CharField(max_length=100, default='',  blank=True)
   stratergy_body = models.TextField(blank=True)
   staff = models.OneToOneField(Staff, on_delete=models.CASCADE, primary_key=True)

class project_images(models.Model):
    image_name = models.CharField(max_length=150, blank=True)
    project_image = models.ImageField(upload_to='project_image', blank=True)


class Project(models.Model):
   
   project_title = models.CharField(max_length=100, default='',  blank=True)
   project_detail = models.TextField(blank=True)
   project_summary = models.TextField(blank=True)
   project_results = models.TextField(blank=True)
   client = models.CharField(max_length=100, default='',  blank=True)
   Surface_area = models.CharField(max_length=100, default='',  blank=True)
   date_of_finish = models.DateField(blank=True, null=True)
   project_cost = models.DecimalField(max_digits=10, decimal_places=2)
  
   service_surface = models.CharField(max_length=100, default='',  blank=True)
   location = models.CharField(max_length=100, default='',  blank=True)
   p_image = models.ImageField(upload_to='p_image', blank=True)
   
   

   def get_absolute_url(self):
    return reverse("cepat:project-detail",  kwargs={"pk": self.pk})



   def __str__(self):
       return str(self.project_title) + ":$"+ str(self.project_cost)




class news(models.Model):
    news_title = models.CharField(max_length=225, blank=True)  
    news_body = models.TextField(blank=True)
    news_subtitle = models.CharField(max_length=255, blank=True)
    news_image = models.ImageField(upload_to='news_image', blank=True) 
    clip = models.FileField(upload_to='videos', null=True) 
    author = models.CharField(max_length=255, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.news_title)   

    def get_absolute_url(self):
      return reverse("cepat:news-detail",  kwargs={"pk": self.pk})


class Book(models.Model):
    title = models.CharField(max_length=225 )
    author = models.CharField(max_length= 255)
    pdf = models.FileField(upload_to='books/pdfs')


    def __str__(self):
        return self.title



class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"