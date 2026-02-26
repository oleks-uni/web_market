from rest_framework import serializers
from .models import ItemModel
from datetime import date

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = [
            'id',
            'name',
            'description',
            'amount',
            'price_per_one_item',
            'full_price',
            'expires_at',
            'created_at',
            'updated_at',
        ]

        read_only_fields = ['id', 'full_price', 'created_at', 'updated_at']


    def validate(self, attr):
        price = round(attr.get('price_per_one_item'), 2)
        amount = attr.get('amount')
        expires_at = attr.get('expires_at')

        if expires_at:
            if expires_at < date.today():
                raise serializers.ValidationError({
                    'error': f"You cannot add an expired item. You got: '{expires_at}' / Today's date '{date.today()}'"
                    })
   
        if price or price == 0:
            if price < 0:
                raise serializers.ValidationError({
                    "error": f"Price cannot be less than 0. You got: {price}"
                    })

        if amount:
            if amount < 0:
                raise serializers.ValidationError({
                    "error": f"Amount cannot be less than 0. You got: {amount}"
                    })
 
        return attr