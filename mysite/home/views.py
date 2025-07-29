from django.shortcuts import render

# Create your views here.
def home(request):
    rsp = render(request=request, template_name='home/main.html')
    rsp.set_cookie('dj4e_cookie', 'e6b99ce4', max_age=1000)
    return rsp
