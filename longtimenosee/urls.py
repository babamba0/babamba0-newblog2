"""longtimenosee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from post import views as post
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , post.home , name="home"),
    path('new/', post.new, name="new"),
    path('create/', post.create, name="create"),
    path('read/<int:post_id>/' , post.read,name="read"),
    path('renew/<int:post_id>/' , post.renew , name="renew"),
    path('update/<int:post_id>/' , post.update, name="update"),
    path('delete/<int:post_id>/' , post.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
