from django.shortcuts import render
from rest_framework.views import APIView

class Home(APIView):

  def get(self, request):
    # alessandro@logopedistarigamonti.com, tag a con mail to      OK
    # psicologia dell'età evolutiva / Tutor DSA       OK
    # i nostri servizi, metti foto figure con sfondo bianco, e in mezzo il blu, arancione ecc
    # invece del hr metti 4 pallini con i 4 colori, 87B5C4, C44325, F8B451, 000000      OK
    # nel benvenuti al...metto il portfolio di ale
    # sistemare foto ale nella seconda pagina

    # copia spudoratamente la pagina contatti
    # nel chi siamo link a "perchè sceglierci"
    # mettilo online su mazino
    # fai footer

    # nei servizi copia da alke e metti foto e testi a caso
    # navbar tutto maiuscolo    OK

    return render(request, 'home.html')