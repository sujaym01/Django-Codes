from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_car'),
    path('buy/<int:id>/', views.buy_car, name='buy_car'),
]
