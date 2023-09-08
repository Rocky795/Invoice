"""
URL configuration for Invoice project.

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
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from new import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.view_logout,name="logout"),
    path('addinvoice/',views.addClient,name='addinvoice'),
    path('addservice/',views.addService,name='addservice'),
    path('addcompany/',views.addCompany,name='addcompany'),
    path('updatecompany/<int:id>/',views.updatecompany,name="updatecompany"),
    path('deletecompany/<int:id>/',views.DeleteCompany,name="deletecompany"),
    path('reviewinvoice/',views.ReviewInvoice,name="reviewinvoice"),
    path('reviewinvoice/<int:pk>/',views.view,name="")
]


# urlpatterns+=staticfiles_urlpatterns