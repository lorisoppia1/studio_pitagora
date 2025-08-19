from django.shortcuts import render
from rest_framework.views import APIView

class Home(APIView):

  def get(self, request):
    return render(request, 'home.html')

class ChiSiamo(APIView):

  def get(self, request):
    return render(request, 'chi_siamo.html')
  

# COSE DA FARE
# 1 - nei nostri servizi metti foto figure (triangolo, quadrato, pentagono ecc...) con sfondo bianco e in mezzo il blu, arancione ecc...
# 2 - copia la pagina contatti
# 4 - fai footer OK
# 5 - nel benvenuti al metto il portfolio di ale
# 6 - sistemare foto ale nella seconda pagina
# 7 - metti online su mazino
# 8 - fai pagina chi siamo da gmail