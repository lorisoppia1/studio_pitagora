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

class Logopedia(APIView):

  def get(self, request):
    return render(request, 'logopedia.html')

class Psicoterapia(APIView):

  def get(self, request):
    return render(request, 'psicoterapia.html')

class Psicologia(APIView):

  def get(self, request):
    return render(request, 'psicologia.html')

class TNPEE(APIView):

  def get(self, request):
    return render(request, 'tnpee.html')

class Osteopatia(APIView):

  def get(self, request):
    return render(request, 'osteopatia.html')

class Massoterapia(APIView):

  def get(self, request):
    return render(request, 'massoterapia.html')
 
  

# COSE DA FARE
# 1 - nei nostri servizi metti foto figure (triangolo, quadrato, pentagono ecc...) con sfondo bianco e in mezzo il blu, arancione ecc...