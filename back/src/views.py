from rest_framework import routers, serializers, viewsets
from rest_framework.schemas.openapi import AutoSchema
from .models import Product
class CustomSchema(AutoSchema):
    def map_field(self,field):
        if isinstance(field, serializers.ImageField):
            return {"type":"string"}
        return super().map_field(field)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['name','description','image','price']
    def get_image(self, obj):
        return obj.image.url

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    schema = CustomSchema()
    
