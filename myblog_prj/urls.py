from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('single_pages.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
