from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangonautic import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
