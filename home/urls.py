from django.urls import path
from .views import HomeView, MongardView, PythonTutorialView

app_name='home'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("mongard_view/", MongardView.as_view(), name="mongard_view"),
    path("python/", PythonTutorialView.as_view(), name="python"),
]


