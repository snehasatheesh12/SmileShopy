
from django.conf import settings
from django.urls import path
from products import  views
from django.conf.urls.static import static
urlpatterns = [
           path('',views.index,name="index")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
