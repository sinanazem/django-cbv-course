from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')



class MongardView(View):
    
    def get(self, request):
        return render(request, 'home/mongard_view.html')
    
    
    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['user'] = request.user
        response.headers['user_authenticated_status'] = request.user.is_authenticated
        return response
    
    