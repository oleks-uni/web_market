from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ItemSerializer
from .models import ItemModel
from market.validators import get_object_or_404

class ItemCreateView(APIView):
    
    def get(self, request):
        items = ItemModel.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = serializer.save()
        return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
    

class ItemDetailView(APIView):

    def get_item(self, id):
        item = get_object_or_404(ItemModel, id=id)
        return item
    

    def get(self, requser, id):
        item = self.get_item(id=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    

    def put(self, request, id):
        item = self.get_item(id=id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        item = serializer.save()
        return Response(ItemSerializer(item).data, status=status.HTTP_200_OK)
    
    
    def delete(self, request, id):
        item = self.get_item(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    