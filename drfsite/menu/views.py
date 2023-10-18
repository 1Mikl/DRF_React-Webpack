from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Recipes
from .serializers import CategoriesSerializer, RecipeSerializer, DishesSerializer


class Recipe_view(ReadOnlyModelViewSet):
    queryset = Recipes.objects.all()
    print(queryset)
    serializer_class = RecipeSerializer


class Categories_view(ReadOnlyModelViewSet):
    queryset = Recipes.objects.values('categoryType').distinct()
    serializer_class = CategoriesSerializer


@api_view(['GET'])
def dishes_view(request):
    if request.method == 'GET':
        dishes = Recipes.objects.filter(categoryType=request.query_params['category'])
        serializer = DishesSerializer(dishes, many=True)
        return Response(serializer.data)