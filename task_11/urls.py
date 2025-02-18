
from django.contrib import admin
from django.urls import path
from restaurants import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('restaurants/list/',views.restaurant_list ,name='restaurant-list'),
    path('restaurants/<int:restaurant_id>/detail/',views.restaurant_detail ,name='restaurant-detail'),

    path('restaurants/create/',views.restaurant_create ,name='restaurant-create'),
    path('restaurants/<int:restaurant_id>/update/',views.restaurant_update ,name='restaurant-update'),
    path('restaurants/<int:restaurant_id>/delete/',views.restaurant_delete ,name='restaurant-delete'),

    path('restaurants/<int:restaurant_id>/item/add/',views.item_create ,name='item-create'),

    path('signup/',views.signup ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),

    path('no_access/', views.no_access, name= 'no-access'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)