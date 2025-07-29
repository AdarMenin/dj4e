from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View


class hello(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        KEY = "visit_number"
        request.session[KEY] = request.session.get(KEY, 0) + 1
        if request.session[KEY] >= 5:
            request.session[KEY] = 1
        resp = HttpResponse(f'view count={request.session[KEY]}')
        resp.set_cookie('dj4e_cookie', 'e6b99ce4', max_age=1000)
        return resp