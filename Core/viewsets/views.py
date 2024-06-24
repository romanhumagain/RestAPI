from rest_framework.response import Response
from rest_framework import viewsets
from .models import Item, Comment, Category, Product, Review
from .serializers import CommentSerializer, ItemSerializer, CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework import viewsets, permissions, filters, status, serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

class IsOwner(permissions.BasePermission):
  # custom permission to only allow user to edit or delete it
  def has_object_permission(self, request, view, obj):
    return obj.owner == request.user
  

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  # permission_classes = [permissions.IsAuthenticated,IsOwner]
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  filterset_fields = ['name', 'created_at']
  ordering_fields = ['name', 'created_at']
  ordering = ['-created_at']
  
  FORBIDDEN_KEYWORDS = ["admin", "root", "forbidden"]
  
  def get_queryset(self):
      self.queryset = Item.objects.all()
  
  def perfom_create(self, serializer):
    # custom validation logic before saving an item
    name = serializer.validated_data['name'].lower()
    if any(keyword in name for keyword in self.FORBIDDEN_KEYWORDS):
      raise serializers.ValidationError({"name":"Name contains forbinnder keyword"})
    
    serializer.save(owner = self.request.user)
    return Response({"status":"item Created"}, status=status.HTTP_201_CREATED)
    
  def perform_update(self, serializer):
    # Custom validation logic before updating an item
      name = serializer.validated_data['name'].lower()
      if any(keyword in name for keyword in self.FORBIDDEN_KEYWORDS):
          raise serializers.ValidationError({"name": "Name contains forbidden keyword"})
      serializer.save()
      return Response({'status': 'item updated'}, status=status.HTTP_200_OK)
  
  def perform_destroy(self, instance):
    # custom logic before deleting an item
    instance.delete()
    return Response({"status":"item deleted"}, status= status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
#=========== WORKING WITH VIEWSET CLASS FOR THE E-COMMERSE WEBSITE SCENARIO ===============
class CategoryViewSet(viewsets.ViewSet):
  def list(self, request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many = True)
    return Response(serializer.data)
  
  
  def retrieve(self, request, pk = None):
    queryset = Category.objects.all()
    category = get_object_or_404(queryset, pk = pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk = None):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def partial_update(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def destroy(self, request, pk=None):
      category = get_object_or_404(Category, pk=pk)
      category.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  
class ProductViewSet(viewsets.ViewSet):
  def list(self, request, category_pk=None):
    queryset = Product.objects.filter(category=category_pk)
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None, category_pk=None):
    queryset = Product.objects.filter(pk=pk, category=category_pk)
    product = get_object_or_404(queryset, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

  def create(self, request, category_pk=None):
      data = request.data.copy()
      data['category'] = category_pk
      serializer = ProductSerializer(data=data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk=None, category_pk=None):
      product = get_object_or_404(Product, pk=pk, category=category_pk)
      serializer = ProductSerializer(product, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def partial_update(self, request, pk=None, category_pk=None):
      product = get_object_or_404(Product, pk=pk, category=category_pk)
      serializer = ProductSerializer(product, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None, category_pk=None):
      product = get_object_or_404(Product, pk=pk, category=category_pk)
      product.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(viewsets.ViewSet):
    def list(self, request, category_pk=None, product_pk=None):
      queryset = Review.objects.filter(product__category=category_pk, product=product_pk)
      serializer = ReviewSerializer(queryset, many=True)
      return Response(serializer.data)

    def retrieve(self, request, pk=None, category_pk=None, product_pk=None):
      queryset = Review.objects.filter(pk=pk, product=product_pk, product__category=category_pk)
      review = get_object_or_404(queryset, pk=pk)
      serializer = ReviewSerializer(review)
      return Response(serializer.data)  
    
    def create(self, request, category_pk = None, product_pk = None):
      data = request.data
      data['product'] = product_pk
      serializer = ReviewSerializer(data = data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None, category_pk=None, product_pk=None):
      review = get_object_or_404(Review, pk=pk, product = product_pk, product__category = category_pk)
      serializer = ReviewSerializer(review, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
    def partial_update(self, request, pk=None, category_pk=None, product_pk=None):
        review = get_object_or_404(Review, pk=pk, product=product_pk, product__category=category_pk)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, category_pk=None, product_pk=None):
        review = get_object_or_404(Review, pk=pk, product=product_pk, product__category=category_pk)
        review.delete()
        
        
        
# ========== performing same things using ModelViewSet

# class CategoryViewSet(viewsets.ModelViewSet):
#   queryset = Category.objects.all()
#   serializer_class = CategorySerializer
  
  
# class ProductViewSet(viewsets.ModelViewSet):
#   serializer_class = ProductSerializer
  
#   def get_queryset(self):
#     category_pk = self.kwargs['category_pk']
#     return Category.objects.filter(category = category_pk)
  
#   def create(self, serializer):
#     category_pk = self.kwargs['category_pk']
#     serializer.save(category_pk)
   
# class ReviewViewSet(viewsets.ModelViewSet):
#     serializer_class = ReviewSerializer

#     def get_queryset(self):
#         product_pk = self.kwargs['product_pk']
#         category_pk = self.kwargs['category_pk']
#         return Review.objects.filter(product__category_id=category_pk, product_id=product_pk)

#     def perform_create(self, serializer):
#         product_pk = self.kwargs['product_pk']
#         serializer.save(product_id=product_pk) 
