from django.urls import path
from .views import HomeView, MongardView, PythonTutorialView, HomeDetailView, CreateCarView, DeleteCarView

app_name='home'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", HomeDetailView.as_view(), name="detail"),
    path("create/", CreateCarView.as_view(), name="car_create"),
    path("delete/<int:pk>/", DeleteCarView.as_view(), name="car_delete"),
    path("mongard_view/", MongardView.as_view(), name="mongard_view"),
    path("python/", PythonTutorialView.as_view(), name="python"),
    
]


