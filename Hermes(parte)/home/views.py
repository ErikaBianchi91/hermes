from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *

from datetime import datetime
def home(request):


    return render(request, 'home/homepage1.html')

#creo una lista dei tavoli disponibili(di cui prendo il numero) ed una dei pasti già aperti
def index(request):

    tavoli = Tavolo.objects.all().order_by('numero')
    pasti = Pasto.objects.filter(fine=None).order_by('tavolo__numero')
    id_tavoli_aperti = set([p.tavolo.numero for p in pasti])
    tavoli_disponibili = []
    for t in tavoli:
        if t.numero not in id_tavoli_aperti:
            tavoli_disponibili.append(t)

    return render(request, 'home/home.html', {'tavoli_disponibili': tavoli_disponibili, 'pasti': pasti})


#apro un nuovo pasto segnalando l'orario di inizio ed il numero del tavolo, poi elenco i piatti(di cui prendo gli id)
def apri(request, numero):

    tav = Tavolo.objects.get(numero=numero)
    p = Pasto(tavolo=tav, inizio=datetime.now())
    p.save()
    piatti = Piatto.objects.all().order_by('tipo')

    return render(request, 'home/nuovo.html', {'piatti': piatti, 'tavolo': tav})


#utilizzando il num del tavolo e l'id del piatto dovrei aprire un nuovo ordine
def aggiunta (request,numero,id_piatto) :
    tav=Tavolo.objects.get(numero=numero)
    lista_piatti=Piatto.objects.filter(id=id_piatto)
    for pietanza in lista_piatti:
        piatti=Piatto.objects.get(nome=pietanza)
        o = Ordinazione(tavolo=tav, orario_richiesta=datetime.now(),nome_piatto=piatti)
        o.save()

    return HttpResponseRedirect('/apri/{}'.format(numero))


#pagina cucina per visualizzare gli ordini
def cucina(request):
    ordinazioni = Ordinazione.objects.filter(orario_cottura=None).order_by('orario_richiesta')
    return render(request, 'home/cucina.html', {'ordinazioni': ordinazioni})

#comando cottura
def cottura(request,id):

    ordine= Ordinazione.objects.filter(id=id).update( orario_cottura=datetime.now())

    return HttpResponseRedirect('/cucina/')


