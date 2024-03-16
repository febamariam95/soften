"""
URL configuration for soften project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show',views.show),
    path('disp/<int:d>/<int:g>',views.disp),
    path('home',views.home),
    path('ind',views.ind),
    path('index',views.index),
    path('reg',views.reg),
    path('display',views.display),
    path('delete/<int:d>',views.delete),
    path('update/<int:d>',views.update),
    path('login',views.login),

    path('userhome',views.userhome),
    path('adminhome',views.adminhome),
    path('addproduct',views.addproduct),
    path('displayproduct',views.display_product),
    path('deleteproduct/<int:d>',views.delete_product),
    path('updateproduct/<int:d>',views.update_product),
    path('userdetails',views.user_details),
    path('logout',views.logout),
    path('addcart/<int:d>',views.add_to_cart),
    path('displaycart',views.display_cart),
    path('normal',views.normal_form),
    path('model',views.mform),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)