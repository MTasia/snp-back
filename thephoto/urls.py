from django.urls import path
from .views import HomeView, PhotoDetailsView, AddPhotoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>', PhotoDetailsView.as_view(), name='detail'),
    path('add_photo', AddPhotoView.as_view(), name='add_photo')
]
