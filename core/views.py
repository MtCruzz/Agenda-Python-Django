from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.
def retorna_data (request, titulo_evento):
    tit = Evento.objects.get(titulo = titulo_evento)
    return HttpResponse('<h1>Data do evento: {}</h1>'.format(tit.data_evento))

def lista_eventos(request):
    evento = Evento.objects.all()
    response = {'eventos':evento}
    return render(request, 'agenda.html',response)