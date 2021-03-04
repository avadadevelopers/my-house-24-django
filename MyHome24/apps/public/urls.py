from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='public_index'),
    path('about', views.index_view, name='public_about'),
    path('services', views.index_view, name='public_services'),
    path('contact', views.index_view, name='public_contact'),
    path('about', views.index_view, name='public_about'),
    path('error', views.index_view, name='public_error'),
    # path('account/', views.index_view, ),
]