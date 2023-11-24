from django.urls import path
from .views import id_pasaporte, id_pais, id_continente

urlpatterns = [
    path('pasaportecrudo/<int:id_pasaporte>/', id_pasaporte, name='id_pasaporte'),
    path('pasaportes/paiscrudo/<int:id_pais>/', id_pais, name='by_id_pais'),
    path('pasaportes/continentecrudo/<int:id_continente>/', id_continente, name='id_continente'),
]
