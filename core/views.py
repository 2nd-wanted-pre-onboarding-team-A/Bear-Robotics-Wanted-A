# from restaurant.models import Restaurant
# from .serializers import RestaurantSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response


# class PaymentKpiView(APIView):
#     def get(self, request, format=None):
#         restaurant = get_object_or_404(Restaurant)
#         serializer = RestaurantSerializer(restaurant, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)