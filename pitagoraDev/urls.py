from django.urls import path
from pitagoraDev.views import *

urlpatterns = [
  path('', Home.as_view()),
  path('chi-siamo', ChiSiamo.as_view())
] 