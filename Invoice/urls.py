
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