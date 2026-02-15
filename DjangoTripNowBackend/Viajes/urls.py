from django.urls import path

from Viajes.views import AddViajeView, ViajeView, CategoriaView

urlpatterns = [
    path('crear-viaje/', AddViajeView.as_view()),

    path('todos-viajes/', ViajeView.as_view() ),

    path('categorias/', CategoriaView.as_view()),

]