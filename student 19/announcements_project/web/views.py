from django.views import View
from django.shortcuts import render

# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'web/home.html')