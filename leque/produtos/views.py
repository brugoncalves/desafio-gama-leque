from django.http import HttpResponse


def index(request):
    return HttpResponse("Bem vindo ao Django Ladies!")


def find_by_id(request, product_id):
    return HttpResponse(f'Id do produto: {product_id}')
