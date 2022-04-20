from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    # /posts/
    path('', views.index, name='index'),

    # /posts/create/
    path('create/', views.product_create, name='product_create'),

    # /posts/update/
    path('<int:product_id>/update/', views.product_update, name='product_update'),

    #/posts/delete/
    path('<int:product_id>/delete/', views.product_delete, name='product_delete'),

    # /posts/search/
    path('search/', views.search, name='product_search')
]