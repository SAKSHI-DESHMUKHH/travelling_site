from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homePage,name="home"),
    path('dest/<int:dest_id>',views.dest_details,name="dest"),
    path('add',views.dest_add,name='add_destination'),
    
    path('api/dests/',views.get_all_destinations,name="destination_list"),
    path('api/dests_detail/<str:pk>/',views.destinations_detail,name="destination_detail"),
    path('api/dests_create/',views.destinations_create,name="destination_create"),
    path('api/dests_update/<str:pk>/',views.destinations_update,name="destination_update"),
    path('api/dests_delete/<str:pk>/',views.destinations_delete,name="destination_delete"),
    path('view',views.view_profile),
    path('update/<str:pk>/',views.update_profile, name="update"),
    path('delete/<str:pk>',views.delete_profile,name="delete"),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)