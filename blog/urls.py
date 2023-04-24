from django.urls import path

from blog import views
# blog/
urlpatterns = [
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.detail),
    path('<int:pk>/', views.PostDetail.as_view()),
]
