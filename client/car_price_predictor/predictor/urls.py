from django.urls import path
from django.urls import include, re_path
from predictor.views import Home, predict
from . import views


urlpatterns = [
    re_path('index',Home),
    
    re_path('predict',predict),
]