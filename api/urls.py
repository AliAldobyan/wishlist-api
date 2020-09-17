from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from api import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api-login"),
    path('register/', views.Register.as_view(), name="api-register"),

    path('items/', views.ItemListView.as_view(), name="api-list"),
    path('items/<int:item_id>/', views.ItemDetailView.as_view(), name="api-detail"),
]
