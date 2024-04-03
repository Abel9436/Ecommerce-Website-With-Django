from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.signin,name='login'),
    path('logout',views.signout,name='logout')
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
