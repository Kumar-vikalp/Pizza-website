"""
URL configuration for pizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Pizza_app.views import home, about, register, login, pizza_list, pizza_edit, pizza_delete, menu, book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('about/', about),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('pizza/', pizza_list, name='pizza'),
    path('pizza/edit/<int:id>/', pizza_edit, name='pizza_edit'),
    path('pizza/delete/<int:id>/', pizza_delete, name='pizza_delete'),
    path('menu/', menu, name='menu'),
    path('book/', book, name='menu'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)