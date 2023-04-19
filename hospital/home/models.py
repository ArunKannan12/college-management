from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class departments(models.Model):
    depts=models.CharField(max_length=100)
    def __str__(self):
        return self.depts
class staffdetail(models.Model):
    staff_name=models.CharField(max_length=100)
    depts=models.ForeignKey(departments,on_delete=models.CASCADE,null=True)
    staff_image=models.ImageField(upload_to='staff_images',null=True)
    def __str__(self):
        return self.staff_name.capitalize()
class hods(models.Model):
    hod_name=models.CharField(max_length=100)
    depts=models.ForeignKey(departments,on_delete=models.CASCADE,null=True)
    hod_image=models.ImageField(upload_to='hod_images',null=True)
    def __str__(self):
        return self.hod_name.capitalize() + " ( " + str(self.depts) + " )"
class admission(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=50)
    date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    email=models.EmailField(max_length=254)
    GENDER=(('MALE','MALE'),('FEMALE','FEMALE'))
    gender=models.CharField(max_length=50,choices=GENDER,null=True)
    phone=models.CharField(max_length=10)
    address=models.TextField(max_length=200,null=True)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    pin=models.CharField(max_length=6,null=True)
    COURSES=(('B.SC.GEOGRAPHY','B.SC.GEOGRAPHY'),('B.SC.MICROBIOLOGY','B.SC.MICROBIOLOGY'),('B.SC.COMPUTER SCIENCE','B.SC.COMPUTER SCIENCE'),('B.SC.PHYSICS','B.SC.PHYSICS'),('B.SC.MATHEMATICS','B.SC.MATHEMATICS'),('B.COM IT','B.COM IT'),('B.COM CA','B.COM CA'),('B.COM','B.COM'),('B.B.A BUSINESS ADMINISTRATION','B.B.A BUSINESS ADMINISTRATION'),('BBA.CA','BBA.CA'),('B.A ENGLISH','B.A ENGLISH'),('B.COM','B.COM'),('B.Sc.Cs','B.Sc.Cs'),('BCA','BCA'))
    courses_available=models.CharField(max_length=50,choices=COURSES,null=True)
    image=models.ImageField(upload_to='sample_images',null=True,blank=True)



    def __str__(self):
        return self.firstname.capitalize() + " " + self.lastname.capitalize()
    
    @property
    def imageURL(self):
        try:
            URL=self.image.url
        except:
            URL=''
        return URL
# class photo(models.Model):
#     image=models.ImageField(upload_to='sample_images', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    