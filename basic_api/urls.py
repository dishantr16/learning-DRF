from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from basic_api import views

urlpatterns = [
    path('basic/', views.API_Objects.as_view()),
    path('basic/<int:pk>/', views.API_Objects_Details.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)