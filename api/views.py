from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, ItemSerializer, ItemDetailsSerializer
from items.models import Item, FavoriteItem
from rest_framework.filters import SearchFilter, OrderingFilter


class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
