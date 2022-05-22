from django.views.generic import ListView, DetailView, CreateView
from thephoto.models import Photo


class HomeView(ListView):
    model = Photo
    template_name = 'home.html'


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photo_details.html'


class AddPhotoView(CreateView):
    model = Photo
    template_name = 'add_photo.html'
    fields = '__all__'
