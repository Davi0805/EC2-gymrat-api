from django.urls import path
from . import views

urlpatterns = [
    path('ficha/', views.FichanameListView.as_view(), name='ficha-lista'),
    path('ficha/create/', views.FichanameCreateView.as_view(), name='ficha-create'),
    path('exerc/', views.ExercparametrosListView.as_view(), name='exerc-lista'),
    path('exerc/create/', views.ExercparametrosCreateView.as_view(), name='exerc-create'),
    path('exerc/update/', views.ExercparametrosUpdateView.as_view(), name='exerc-update'),
    path('log/', views.LogListView.as_view(), name='log-lista'),
    path('log/create/', views.LogCreateView.as_view(), name='log-create'),
]