from django.urls import path
from . import views
from django.conf import settings # new
from  django.conf.urls.static import static #new        

urlpatterns = [
    path('ficha/', views.FichanameListView.as_view(), name='ficha-lista'),
    path('ficha/create/', views.FichanameCreateView.as_view(), name='ficha-create'),
    path('exerc/', views.ExercparametrosListView.as_view(), name='exerc-lista'),
    path('exerc/create/', views.ExercparametrosCreateView.as_view(), name='exerc-create'),
    path('exerc/update/', views.ExercparametrosUpdateView.as_view(), name='exerc-update'),
    path('log/', views.LogListView.as_view(), name='log-lista'),
    path('log/create/', views.LogCreateView.as_view(), name='log-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)      