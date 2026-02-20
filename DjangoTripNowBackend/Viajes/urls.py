from django.urls import path

from Viajes.views import AddViajeView, ViajeView, CategoriaView, CategoriaAlojamientoView, AddAlojamientoView, AlojamientoView, ReseñaView

urlpatterns = [
    path('crear-viaje/', AddViajeView.as_view()),

    path('todos-viajes/', ViajeView.as_view() ),

    path('categorias/', CategoriaView.as_view()),

    path('categorias-alojamiento/', CategoriaAlojamientoView.as_view()),

    path('todos-alojamientos/', AlojamientoView.as_view()),

    path('crear-alojamiento/', AddAlojamientoView.as_view()),

    path('todos-resenias/',ReseñaView.as_view() ),
]