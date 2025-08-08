from django.shortcuts import render

from django.contrib.auth.views import LogoutView


# Create your views here.
def home(request):
    rsp = render(request=request, template_name="home/main.html")
    rsp.set_cookie("dj4e_cookie", "e6b99ce4", max_age=1000)
    return rsp


class LogoutAllowGetView(LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
