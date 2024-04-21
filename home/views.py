from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView, CreateView, DeleteView, UpdateView
from .models import Car
from .forms import CarAddForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_views


class UserLogin(auth_views.LoginView):
    template_name = "home/login.html"
    next_page = reverse_lazy('home:home')
    
class UserLogout(auth_views.LogoutView):
    next_page = reverse_lazy('home:home')


# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home/home.html')

# class HomeView(TemplateView):
#     template_name = "home/home.html"
    
#     def get_context_data(self, **kwargs: Any):
#         context_data =  super().get_context_data(**kwargs)
#         context_data['cars'] = Car.objects.all()
#         return context_data

class HomeView(ListView):
    template_name = "home/home.html"
    # model = Car
    # queryset = Car.objects.filter(year__gte=2023)
    context_object_name = 'cars'
    ordering = ('-year',)
    
    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(year__gte=2023)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['username'] = 'jack'
        return context

class HomeDetailView(DetailView):
    template_name = "home/detail.html"
    model = Car

# class CreateCarView(FormView):
#     template_name = "home/create.html"
#     form_class = CarAddForm
#     success_url = reverse_lazy('home:home')
    
#     def form_valid(self, form):
#         self._create_car(form.cleaned_data)
#         messages.success(self.request, 'create car successfully', 'success')
#         return super().form_valid(form)
    
#     def _create_car(self, data):
#         Car.objects.create(name=data['name'], owner=data['owner'], year=data['year'])

class DeleteCarView(DeleteView):
    template_name = 'home/delete.html'
    model = Car
    success_url = reverse_lazy('home:home')


class UpdateCarView(UpdateView):
    template_name = 'home/update.html'
    model = Car
    success_url = reverse_lazy('home:home')
    fields =  ('name',)

class CreateCarView(CreateView):
    model = Car
    fields = ('name', 'year')
    template_name = "home/create.html"
    success_url = reverse_lazy('home:home')
    
    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user.username if self.request.user.username else "nothing"
        car.save()
        messages.success(self.request, 'create car successfully', 'success')
        return super().form_valid(form)
    


class MongardView(View):
    
    http_method_names = ["post", "options"]
    
    def post(self, request):
        return render(request, 'home/mongard_view.html')
    
    
    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['user'] = request.user
        response.headers['user_authenticated_status'] = request.user.is_authenticated
        return response
    
    def http_method_not_allowed(self, request: HttpRequest, *args: Any, **kwargs: Any):
        
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, 'home/http_method_not_allowed.html')


class PythonTutorialView(RedirectView):
    # url = 'https://www.pytopia.ai/'
    pattern_name = 'home:mongard_view'
    query_string = True
    
    def get_redirect_url(self, *args, **kwargs):
        print("+" * 50)
        return super().get_redirect_url(*args, **kwargs)