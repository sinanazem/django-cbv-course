from django.urls import path
from .views import HomeView, MongardView, PythonTutorialView, HomeDetailView, CreateCarView, DeleteCarView, UpdateCarView, UserLogin, UserLogout

app_name='home'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", HomeDetailView.as_view(), name="detail"),
    path("create/", CreateCarView.as_view(), name="car_create"),
    path("update/<int:pk>/", UpdateCarView.as_view(), name="car_update"),
    path("delete/<int:pk>/", DeleteCarView.as_view(), name="car_delete"),
    path("mongard_view/", MongardView.as_view(), name="mongard_view"),
    path("python/", PythonTutorialView.as_view(), name="python"),
    path("login/", UserLogin.as_view(), name="user_login"),
    path("logout/", UserLogout.as_view(), name="user_logout"),
    
]


