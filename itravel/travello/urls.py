from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homePage,name="home"),
    path('dest/<int:dest_id>',views.dest_details,name="dest"),
    path('view',views.view_profile),
    path('edit',views.edit_profile),
    path('delete',views.delete_profile),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)