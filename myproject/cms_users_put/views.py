from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cms_users_put(request, recurso):

    status = "<p><a href='/admin/logout/'>Logout</a></p>"
    if not request.user.is_authenticated():
       return HttpResponse("<p>No esta logueado <a href='/admin/login/'> Para loguearse</a><p>")
    if request.method == 'GET':
        try:
            pages = Pages.objects.get(name=recurso)
            return HttpResponse("pagina de " + pages.page + status)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Recurso no encontrado" + status)
    elif request.method == 'PUT':
            p = Pages(name=recurso, page=request.body)
            p.save()
            return HttpResponse("Pagina guardada: " + request.body)
    else:
        return HttpResponseNotFound("metodo no disponible")
