from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('itemPage/<int:pk>/', views.itemView, name='itemView'),
    path('qrCodesPage/', views.qrCodeList, name='qrCodeList'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
