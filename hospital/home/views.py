from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

def signinpage(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"registration successfull 🤩 "  + user)
            return redirect('loginpage')
    context={
        'form':form
        }
    return render (request,'signup.html',context)
def loginpage(request):
   
    if request.method == 'POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfull 🤗")
            return redirect('home')
        else:
            messages.info(request,"Please check the username and password 😐")
            return redirect('loginpage')
    return render (request,'loginpage.html')
def logoutpage(request):
    logout(request)
    messages.success(request,"you have been successfully logged out from this page 😊 ")
    return redirect('loginpage')
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def staffdetails(request):
    detail={
        'dict_staff':staffdetail.objects.all(),
        'hods':hods.objects.all()
    }
    return render(request,'staff details.html',detail)
def about(request):
    return render(request,'about.html')
def addstudents(request):
    form=stadm()
    if request.method == 'POST':
        form=stadm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'student added successfully')
            return redirect('addstudents')
    else:
        form=stadm()        
    context={
        'form':form
    }
    
    return render(request,'add students.html',context)
def studentsdetails(request):
    # bca=admission.objects.filter(courses_available='BCA')
    # if 'q' in request.GET:
    #     q=request.GET['q']
    #     data=admission.objects.filter(firstname__icontains=q)
    # else:
    #     data=admission.objects.all()
    # students_length=len(data)
    # context={
    #     'data':data,'students_length':students_length,'bca':bca
    # }
    return render(request,'students details.html')
# def uploadphoto(request):
#     form=imageupload()
#     if request.method == 'POST':
#         form=imageupload(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
    
#     else:
#         form=imageupload()
#     context={
#         'form':form
#         }   
#     print(form)
#     return render(request,"sample.html",context)
def BCA(request):
    bca=admission.objects.filter(courses_available='BCA')
    if 'q' in request.GET:
        q=request.GET['q']
        bca=admission.objects.filter(firstname__icontains=q,courses_available='BCA')
    else:
        bca=admission.objects.filter(courses_available='BCA')
        
    students_length=len(bca)
    context={
        'bca':bca,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_SC_GEOGRAPHY(request):
    bsc_geo=admission.objects.filter(courses_available='B.SC.GEOGRAPHY')
    if 'q' in request.GET:
        q=request.GET['q']
        bsc_geo=admission.objects.filter(firstname__icontains=q,courses_available='B.SC.GEOGRAPHY')
    else:
        bsc_geo=admission.objects.filter(courses_available='B.SC.GEOGRAPHY')
    students_length=len(bsc_geo)
    context={
        'bsc_geo':bsc_geo,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_SC_MICROBIOLOGY(request):
    bsc_micro=admission.objects.filter(courses_available='B.SC.MICROBIOLOGY')
    if 'q' in request.GET:
        q=request.GET['q']
        bsc_micro=admission.objects.filter(firstname__icontains=q,courses_available='B.SC.MICROBIOLOGY')
    else:
        bsc_micro=admission.objects.filter(courses_available='B.SC.MICROBIOLOGY')
    students_length=len(bsc_micro)
    context={
        'bsc_micro':bsc_micro,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_SC_COMPUTER_SCIENCE(request):
    bsc_cs=admission.objects.filter(courses_available='B.SC.COMPUTER SCIENCE')
    if 'q' in request.GET:
        q=request.GET['q']
        bsc_cs=admission.objects.filter(firstname__icontains=q,courses_available='B.SC.COMPUTER SCIENCE')
    else:
        bsc_cs=admission.objects.filter(courses_available='B.SC.COMPUTER SCIENCE')
    students_length=len(bsc_cs)
    context={
        'bsc_cs':bsc_cs,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_SC_PHYSICS(request):
    bsc_physics=admission.objects.filter(courses_available='B.SC.PHYSICS')
    if 'q' in request.GET:
        q=request.GET['q']
        bsc_physics=admission.objects.filter(firstname__icontains=q,courses_available='B.SC.PHYSICS')
    else:
        bsc_physics=admission.objects.filter(courses_available='B.SC.PHYSICS')
    students_length=len(bsc_physics)
    context={
        'bsc_physics':bsc_physics,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_SC_MATHEMATICS(request):
    bsc_maths=admission.objects.filter(courses_available='B.SC.MATHEMATICS')
    if 'q' in request.GET:
        q=request.GET['q']
        bsc_maths=admission.objects.filter(firstname__icontains=q,courses_available='B.SC.MATHEMATICS')
    else:
        bsc_maths=admission.objects.filter(courses_available='B.SC.MATHEMATICS')
    students_length=len(bsc_maths)
    context={
        'bsc_maths':bsc_maths,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_COM_IT(request):
    bcom_it=admission.objects.filter(courses_available='B.COM IT')
    if 'q' in request.GET:
        q=request.GET['q']
        bcom_it=admission.objects.filter(firstname__icontains=q,courses_available='B.COM IT')
    else:
        bcom_it=admission.objects.filter(courses_available='B.COM IT')
    students_length=len(bcom_it)
    context={
        'bcom_it':bcom_it,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_COM_CA(request):
    bcom_ca=admission.objects.filter(courses_available='B.COM CA')
    if 'q' in request.GET:
        q=request.GET['q']
        bcom_ca=admission.objects.filter(firstname__icontains=q,courses_available='B.COM CA')
    else:
        bcom_ca=admission.objects.filter(courses_available='B.COM CA')
    students_length=len(bcom_ca)
    context={
        'bcom_ca':bcom_ca,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
def B_COM(request):
    bcom=admission.objects.filter(courses_available='B.COM')
    if 'q' in request.GET:
        q=request.GET['q']
        bcom=admission.objects.filter(firstname__icontains=q,courses_available='B.COM')
    else:
        bcom=admission.objects.filter(courses_available='B.COM')
    students_length=len(bcom)
    context={
        'bcom':bcom,
        # 'data':data,
        'students_length':students_length
    }
    return render(request,'courses.html',context)
