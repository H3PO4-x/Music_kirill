
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('genres',views.music),
    path('track',views.track),
    path ('deleteop/<int:id_genres>',views.deleteop),
    path ('deletetrack/<int:id_track>',views.deletetrack),
    path ('add_genre/',views.add_genre),
    path ('edit_genre/<int:id_genre>',views.edit_genre),
    path ('add_track/',views.add_track),
    path ('edit_track/<int:id_track>',views.edit_track),
    path('artists/',views.artists),
]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
