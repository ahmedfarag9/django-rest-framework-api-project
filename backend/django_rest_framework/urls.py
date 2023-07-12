from django.urls import path
from django.contrib import admin
from core import views as core_views
from ecommerce import views as ecommerce_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


# Import necessary modules
router = routers.DefaultRouter()

# Register viewsets for the router
router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')

# Set urlpatterns to the router's urls
urlpatterns = router.urls

# Add additional paths to urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),  # Endpoint for contact form
    path('api-token-auth/', obtain_auth_token),  # Endpoint for obtaining authentication token
]