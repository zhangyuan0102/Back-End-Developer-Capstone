from django.shortcuts import render
from rest_framework import generics
from .models import Menu,Booking
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
def index(request):
    return render(request, 'index.html', {})
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated] 

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 