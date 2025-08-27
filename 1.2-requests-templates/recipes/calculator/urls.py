from django.urls import path
from . import views

urlpatterns = [
    path('<slug:recipe_name>/', views.recipe_view, name='recipe'),
]
