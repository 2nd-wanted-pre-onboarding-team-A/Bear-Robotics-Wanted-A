from kpi.models import PosResultData
from .models import Restaurant
from .serializers import (
    PosDataListSerializer, PosDataDetailSerializer,
    RestaurantListSerializer, RestaurantDetailSerializer,
)
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class PosDataListView(GenericAPIView):
    queryset = PosResultData.objects.all()
    serializer_class = PosDataListSerializer

    """
        Pos 데이터 리스트조회(GET)
    """
    @swagger_auto_schema(tags=['get all pos datas'], responses={200: 'Success', 404: 'Not Found'})
    def get(self, _, format=None):
        pos_data = self.get_queryset()
        serializer = self.get_serializer(pos_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
        Pos 데이터 추가(POST)
    """
    @swagger_auto_schema(tags=['create pos data'], responses={201: 'Created', 400:'Bad Request'})
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PosDataDetailView(GenericAPIView):
    queryset = PosResultData.objects.all()
    serializer_class = PosDataDetailSerializer

    """
        Pos데이터의 개별 조회(GET)
    """
    @swagger_auto_schema(tags=['get one pos data'], responses={200: 'Success', 404: 'Not Found'})
    def get(self, _, pk, format=None):
        pos_data = self.get_object()
        serializer = self.get_serializer(pos_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantListView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

    """
        Restaurant 테이블 리스트조회(GET)
    """
    @swagger_auto_schema(tags=['get all Restaurants'], responses={200: 'Success', 404: 'Not Found'})
    def get(self, _, format=None):
        restaurants = self.get_queryset()
        serializer = self.get_serializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
        Restaurant 테이블 데이터 추가(POST)
    """
    @swagger_auto_schema(tags=['create Restaurant data'], responses={201: 'Created', 400:'Bad Request'})
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailView(GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer

    """
        Restaurant 테이블 개별조회(GET)
    """
    @swagger_auto_schema(tags=['get one Restaurant'], responses={200: 'Success', 404: 'Not Found'})
    def get(self, _, pk, format=None):
        restaurant = self.get_object()
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
        Restaurant 테이블 수정(PUT)
    """ 
    @swagger_auto_schema(tags=['update one Restaurant'], responses={200: 'Success', 404: 'Not Found', 400: 'Bad Request'})
    def put(self, request, *args, **kwargs):
        restaurant = self.get_object()
        serializer = self.get_serializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
        Restaurant 테이블 삭제(DELETE)
    """
    @swagger_auto_schema(tags=['delete one Restaurant'], responses={200: 'Success', 404: 'Not Found', 400: 'Bad Request'})
    def delete(self, _, pk, format=None):
        restaurant = self.get_object()
        restaurant.delete()
        return Response(status=status.HTTP_200_OK)