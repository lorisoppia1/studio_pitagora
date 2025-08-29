from django.shortcuts import render
from rest_framework.views import APIView

class Home(APIView):

  def get(self, request):
    return render(request, 'home.html')

class ChiSiamo(APIView):

  def get(self, request):
    return render(request, 'chi_siamo.html')

class Contatti(APIView):

  def get(self, request):
    return render(request, 'contatti.html')
  

# COSE DA FARE
# 1 - nei nostri servizi metti foto figure (triangolo, quadrato, pentagono ecc...) con sfondo bianco e in mezzo il blu, arancione ecc...