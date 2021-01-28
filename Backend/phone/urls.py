from django.urls import path
from .views import index, create, delete, edit, detail



app_name = 'phone'

urlpatterns = [
    path('', index, name = 'index'),
    path('create/', create, name = 'create'),
    path('delete/<int:id>', delete, name = 'delete'),
    path('edit/<int:id>', edit, name = 'edit'),
    path('detail/<int:id>', detail, name = 'detail'),
]
