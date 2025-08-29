from django.urls import path
from pitagoraDev.views import *

urlpatterns = [
  path('', Home.as_view()),
  path('chi-siamo', ChiSiamo.as_view()),
  path('contatti', Contatti.as_view()),
  path('logopedia', Logopedia.as_view()),
  path('psicoterapia', Psicoterapia.as_view()),
  path('psicologia', Psicologia.as_view()),
  path('tnpee', TNPEE.as_view()),
  path('osteopatia', Osteopatia.as_view()),
  path('massoterapia', Massoterapia.as_view())
] 