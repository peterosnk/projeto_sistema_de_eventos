from django.urls import path
from . import views

app_name = 'app_siseventos'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('meus-eventos/', views.meus_eventos, name='meus_eventos'),

    path('evento/novo/', views.cadastrar_evento, name='cadastrar_evento'),
    path('evento/<int:evento_id>/inscrever/', views.inscrever_evento, name='inscrever_evento'),

    path('evento/<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('evento/<int:evento_id>/deletar/', views.deletar_evento, name='deletar_evento'),

    path('evento/<int:evento_id>/cancelar/', views.cancelar_inscricao, name='cancelar_inscricao'),
    path('evento/<int:evento_id>/inscritos/', views.inscritos_evento, name='inscritos_evento'),
    path('evento/<int:evento_id>/encerrar/', views.encerrar_evento, name='encerrar_evento')
]