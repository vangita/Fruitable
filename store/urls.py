from django.urls import path
from .views import (
    HomeView,
    ContactView,
    CategoryListingView,
    ProductDetailView,
    TestimonialView,
    Custom404View,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/', ProductDetailView.as_view(), name='product_detail'),
    # path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail_slug'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/', CategoryListingView.as_view(), name='generic_category_listing'),
    path('category/<slug:slug>/', CategoryListingView.as_view(), name='category_listing'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('404/', Custom404View.as_view(), name='get404'),
]
