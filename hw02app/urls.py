from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/<int:days>/', views.ordered_products, name='ordered_products'),
    path('<int:customer_id>/', views.customer_name, name='customer_name'),
    path('create/', views.create_product, name='create_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('products/', views.products_list, name='products'),
    path('product/<int:product_id>/', views.product_page, name='product_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)