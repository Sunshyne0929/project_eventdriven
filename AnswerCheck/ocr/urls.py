from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ocr/', views.ocr_view, name='ocr_view'),
    path('process/', views.ocr_process, name='ocr_process'),
]
