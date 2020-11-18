"""magalu_transforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.index, name='shopping_list-index'),
		path('add/', views.add_new_item, name='shopping_list-add'),
		 path('bought/<item_id>', views.bought_item, name='shopping_list-bought'),
		 path('delete_item/', views.delete_item, name='shopping_list-delete'),
		 path('delete_all/', views.delete_all, name='shopping_list-delete_all'),
]
		
