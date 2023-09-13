
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('todolist/',include('todolist.urls')),
    path('admin/', admin.site.urls),
]
