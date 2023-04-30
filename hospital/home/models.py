from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
alpha=RegexValidator(r'^[a-zA-Z]{3,}','only alphabets are allowed and name should be more tha 3 charachets')
numbers=RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$','Enter a Valid Indian Phone Number')
pincode=RegexValidator('^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$','Enter a valid pin code')
# Create your models here.
class departments(models.Model):
    depts=models.CharField(max_length=100)
    def __str__(self):
        return self.depts
class staffdetail(models.Model):
    staff_name=models.CharField(max_length=100,validators=[alpha],null=True,blank=True)
    depts=models.ForeignKey(departments,on_delete=models.CASCADE,null=True)
    staff_image=models.ImageField(upload_to='staff_images',null=True)
    def __str__(self):
        return self.staff_name.capitalize()
class hods(models.Model):
    hod_name=models.CharField(max_length=100,validators=[alpha],null=True,blank=True)
    depts=models.ForeignKey(departments,on_delete=models.CASCADE,null=True)
    hod_image=models.ImageField(upload_to='hod_images',null=True)
    def __str__(self):
        return self.hod_name.capitalize() + " ( " + str(self.depts) + " )"
class admission(models.Model):
    
    firstname=models.CharField(max_length=100,validators=[alpha],null=True,blank=True)
    lastname=models.CharField(max_length=50,validators=[alpha],null=True,blank=True)
    date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
    email=models.EmailField(max_length=254)
    GENDER=(('MALE','MALE'),('FEMALE','FEMALE'))
    gender=models.CharField(max_length=50,choices=GENDER,null=True)
    phone=models.CharField(max_length=10,validators=[numbers])
    address=models.TextField(max_length=200,null=True)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    pin=models.CharField(max_length=6,null=True,validators=[pincode])
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
class Feedback(models.Model):
    name=models.CharField(max_length=50,validators=[alpha],null=True,blank=True)
    dept=models.ForeignKey(departments, on_delete=models.CASCADE,blank=False,null=True)
    feedback=models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name