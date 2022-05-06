from .models import PosResultData
from rest_framework import serializers

class RestaurantKpiSerializer(serializers.Serializer):
    """
    RestaurantKpiView Serializer
    """
    start_time  = serializers.CharField(help_text='검색 시작 날짜', required=True)
    end_time    = serializers.CharField(help_text='검색 종료 날짜', required=True)
    time_window = serializers.CharField(help_text='검색 범위', required=True)
    start_price = serializers.CharField(help_text='시작 가격', required=False)
    end_price   = serializers.CharField(help_text='종료 가격', required=False)
    start_number_of_people = serializers.CharField(help_text='시작 구성원 수', required=False)
    end_number_of_people   = serializers.CharField(help_text='종료 구성원 수', required=False)
    restaurant_group = serializers.CharField(help_text='레스토랑 그룹 번호', required=False)

    class Meta:
        model = PosResultData
        fields = (
            "id",
            "timestamp",
            "restaurant",
            "price",
            "number_of_party",
            "payment",
        )
        read_only_fields = []

class PaymentKpiSerializer(serializers.ModelSerializer):
    """
    PaymentKpiView Serializer
    """
    term = serializers.DateTimeField()
    count = serializers.IntegerField()
    
    class Meta:
        model = PosResultData
        fields = ['term','restaurant_id','payment','count']
        read_only_fields = []

class PartyNumberKpiSerializer(serializers.ModelSerializer):
    """
    PartyNumberKpiView Serializer
    """
    term = serializers.DateTimeField()
    count = serializers.IntegerField()
    
    class Meta:
        model = PosResultData
        fields = ['term','restaurant_id','number_of_party','count']
        read_only_fields = []

