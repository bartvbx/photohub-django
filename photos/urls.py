from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoListView.as_view(), name='photo-list'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/add', views.PhotoCreateView.as_view(), name='photo-create'),
    path('photo/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo-delete'),
]