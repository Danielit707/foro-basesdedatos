from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/nuevo/', views.crear_post, name='crear_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
    # CRUD de comentarios
    path('post/<int:post_pk>/comentario/nuevo/', views.crear_comentario, name='crear_comentario'),
    path('comentario/<int:pk>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:pk>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    # Búsqueda y filtros
    path('buscar/', views.buscar_posts, name='buscar_posts'),
]
