from django.contrib.auth.models import User, Group
from rest_framework import serializers
from listings.models import BookingInfo, HotelRoomType, Listing


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['listing_type', 'title', 'country', 'city']


class HotelRoomTypeSerializer(serializers.ModelSerializer):
    hotel = ListingSerializer(read_only=True)

    class Meta:
        model = HotelRoomType
        fields = ['title', 'hotel']


class BookingInfoSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    hotel_room_type = HotelRoomTypeSerializer(read_only=True)

    class Meta:
        model = BookingInfo
        fields = ['price', 'listing', 'hotel_room_type']
        ordering = ['price']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        listing = representation.pop('listing')
        hotel_room_type = representation.pop('hotel_room_type')
        if listing:
            representation.update(listing)
        else:
            representation.update(hotel_room_type['hotel'])
        return representation
