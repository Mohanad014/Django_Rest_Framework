from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import *

class ProductView(APIView):

# Uploading a product p_name, code and price
    def post(self, request):
        new_product = Product_Serializer(data = request.data)

        if new_product.is_valid():
            new_product.save()
            return Response("Data saved")
    
# Getting all products
    def get(self, request):
        all_products = Product.objects.all()
        serialized_product = Product_Serializer(all_products, many=True).data
        print(serialized_product)
        return Response(serialized_product)
   
# Deleting all products 
    def delete(self, request):
        all_products = Product.objects.all()
        for product in all_products:
            product.delete()
        return Response("All Products Deleted")
    

class ProductViewByID(APIView):

# Getting a single product
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product_data = Product_Serializer(product).data
            return Response(product_data)
        except:
            return Response("Product Not Found")

# Updating a single product
    def patch(self, request, id):
        product = Product.objects.get(id=id)
        new_values = Product_Serializer(product, data=request.data, partial=True)
        if new_values.is_valid():
            new_values.save()
            all_products = Product.objects.get(id = id)
            serialized_product = Product_Serializer(all_products).data
            return Response(serialized_product)
    
# Deleting a single product
    def delete(self, request, id):
        productdelete = Product.objects.get(id = id)
        productdelete.delete()
        return Response("Product Deleted")


class CategoryView(APIView):
    
# Uploading a category
    def post(self, request):
        new_category = Category(category_name = request.data['category_name'])
        new_category.save()

        new_category_data = {
            "id": new_category.id,
            "category_name": new_category.category_name
        }
        return Response(new_category_data)

# Getting all categories
    def get(self, request):
        all_categories = Category.objects.all()
        category_data = []
        for category in all_categories:
            single_category = {
            "id": category.id,
            "category_name": category.category_name
            }
            category_data.append(single_category)
        return Response(category_data)

class CategoryViewByID(APIView):

# Getting a single category
    def delete(self, request, id):
        category = Category.objects.get(id = id)
        category.delete()
        return Response("Category Deleted")

