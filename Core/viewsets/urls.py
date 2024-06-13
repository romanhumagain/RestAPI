from django.urls import path, include
from rest_framework_nested import routers
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

# router = routers.DefaultRouter()
# router.register(r'items', ItemViewSet)

# # for the nested routers
# item_router = routers.NestedDefaultRouter(router, r'items', lookup='item')
# item_router.register(r'comments', CommentViewSet, basename='item-comment')

# urlpatters = [
#   path('', include(router.urls)),
#   path('item-comment/', include(item_router.urls)),
# ]


# /categories/
# /categories/{category_pk}/
# /categories/{category_pk}/products/
# /categories/{category_pk}/products/{product_pk}/
# /categories/{category_pk}/products/{product_pk}/reviews/
# /categories/{category_pk}/products/{product_pk}/reviews/{review_pk}/

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')

category_router = routers.NestedDefaultRouter(router, r'categories', lookup='category')
category_router.register(r'products', ProductViewSet, basename='category-products')

product_router = routers.NestedDefaultRouter(category_router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
  path('', include(router.urls)), 
  path('', include(category_router.urls)),
  path('', include(product_router.urls))
]