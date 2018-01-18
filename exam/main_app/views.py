from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import query
from django.db.models import Q

from django.contrib.auth.models import User

from rest_framework import status

from main_app import serializers
from main_app import models
from main_app import permission


# Create your views here.
@api_view()
def shop_category_list(request):
    print(models.CAT)
    return Response([cat[1] for cat in models.CAT])


@api_view(['POST'])
def create_user(request):
    serialized = serializers.UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(generics.ListAPIView):
    serializer_class = serializers.ProductVersionSerializer

    def get_queryset(self):
        qs = models.ProductVersion.objects.all()
        name = self.request.GET.get('name')
        price = self.request.GET.get('price')
        if name is not None or price is not None:
            if name is not None:
                qs = qs.filter(
                    Q(name__icontains=name)
                ).distinct()
            if price is not None:
                qs = qs.filter(
                    Q(price=price)
                ).distinct()
        return qs


class CartView(generics.ListCreateAPIView):
    serializer_class = serializers.CartSerializer
    queryset = models.Cart.objects.all()


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permission.IsOwner, ]
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class OrderUserView(generics.ListAPIView):
    permission_classes = [permission.IsOwner, ]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderCreateView(generics.CreateAPIView):
    permission_classes = [permission.HasAuth, ]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permission.HasAuth, ]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
