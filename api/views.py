from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from items.models import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated, AllowAny




class Register(CreateAPIView):
	serializer_class = RegisterSerializer

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'description']


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsStaffOrOwner]
