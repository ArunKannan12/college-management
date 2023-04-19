from django.urls import path
from . import views
urlpatterns = [
    path("",views.loginpage,name="loginpage"),
    path("signinpage/", views.signinpage, name="signinpage"),
    path("logoutpage/", views.logoutpage, name="logoutpage"),
    path("home/", views.home, name="home"),
    path('staffdetails/',views.staffdetails, name='staffdetails'),
    path('about/',views.about, name='about'),
    path('addstudents/',views.addstudents, name='addstudents'),
    path('studentsdetails/',views.studentsdetails, name='studentsdetails' ),
    path('bca',views.BCA,name='bca'),
    path('bsc_geo',views.B_SC_GEOGRAPHY,name='bscgeo'),
    path('bsc_micro',views.B_SC_MICROBIOLOGY,name='bscmicro'),
    path('bsc_cs',views.B_SC_COMPUTER_SCIENCE,name='bsccs'),
    path('bsc_physics',views.B_SC_PHYSICS,name='bscphysics'),
    path('bsc_maths',views.B_SC_MATHEMATICS,name='bscmaths'),
    path('b_com-it',views.B_COM_IT,name='bcomit'),
    path('b_com_ca',views.B_COM_CA,name='bcomca'),
    path('bcom',views.B_COM,name='bcom'),
]
