from django.urls import path
from . import views
from .views import (ClientListView, ClientUpdateView ,ClientDetailView, ClientDeleteView, ClientCreateView, comment,clientVechicles)


urlpatterns =[
    path('', views.ClientListView.as_view(), name='client_list'),
    path('<int:pk>/edit/', ClientUpdateView.as_view(), name ='client_edit'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name = 'client_delete'),
    path('<int:pk>/', ClientDetailView.as_view(), name = 'client_detail'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('<int:pk>/comment/',views.comment, name='add_comment'),
    path('vechicles/', views.clientVechicles, name='vechicles'),
]