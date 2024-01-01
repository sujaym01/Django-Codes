
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    # path('about/path/<int:id>/', views.about, name = 'about'),
    path('about/', views.about, name = 'about'),
]