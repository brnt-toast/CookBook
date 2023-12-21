from django.http import HttpResponse

# Create your views here.
def home_page_view(response):
    return HttpResponse("Hello, World")
