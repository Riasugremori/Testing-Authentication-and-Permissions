from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from .permissions import IsAuthenticatedToCreate

class ItemViewSet(viewsets.ModelViewSet):
   
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedToCreate]  
    def perform_create(self, serializer):
        
        if self.request.user.is_authenticated:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response(
                {"detail": "Authentication required."}, 
                status=status.HTTP_403_FORBIDDEN  
            )
