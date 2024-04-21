from django.urls import path
from .views import HomeView, MongardView, PythonTutorialView, HomeDetailView

app_name='home'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", HomeDetailView.as_view(), name="detail"),
    path("mongard_view/", MongardView.as_view(), name="mongard_view"),
    path("python/", PythonTutorialView.as_view(), name="python"),
    
]


