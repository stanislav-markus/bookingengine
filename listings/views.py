from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from listings.serializers import BookingInfoSerializer
from listings.models import BookingInfo, BlockDay


class BookingInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        max_price = self.request.query_params.get('max_price')
        check_in = self.request.query_params.get('check_in')
        check_out = self.request.query_params.get('check_out')
        queryset = BookingInfo.objects.all()
        block_days = BlockDay.objects.filter(date__gte=check_in, date__lte=check_out)
        if check_in and check_out:
            queryset = queryset.filter(~Q(block_days__in=block_days))
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        serializer = BookingInfoSerializer(queryset, many=True)
        return Response({'items': serializer.data})
