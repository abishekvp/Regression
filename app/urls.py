from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('regression',views.regression,name="regression"),
    path('on_change',views.on_change,name="on_change"),
]

