from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),

    path('save/', views.saveAction, name='save'),

    path('edit/<int:pk>', views.edit, name='edit'),

    path('delete/<int:pk>', views.deleteAction, name='delete')
]