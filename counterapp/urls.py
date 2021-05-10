from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('increment/',views.increment, name="increment"),
    path('reset/',views.reset, name="reset"),
    path('decrement/',views.decrement, name="decrement"),
    

]
