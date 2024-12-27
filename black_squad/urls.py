from django.contrib import admin  # Correct import
from django.urls import path
from black_squad import settings
from squad import views  # Import views from the app folder
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # Use admin.site.urls
    path('', views.home, name='home'),  # Homepage URL
    path('member/<int:pk>/', views.member_detail, name='member_detail'),  # Member detail page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
