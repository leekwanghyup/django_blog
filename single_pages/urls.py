from django.urls import path, include

from single_pages import views

urlpatterns = [
    path('', views.main),
    path('about_me/', views.about_me),
]
