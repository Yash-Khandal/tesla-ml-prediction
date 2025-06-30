from django.urls import path
from . import views

urlpatterns = [
    path('', views.tesla_prediction_view, name='tesla_prediction'),
    path('api/predict/', views.api_predict, name='api_predict'),
]
