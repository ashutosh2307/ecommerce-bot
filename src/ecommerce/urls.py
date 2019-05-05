
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

# from products.views import ( 
#     ProductListView,from products.views import ( 
#     ProductListView,
#     ProductDetailView,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView,
#     ProductDetailSlugView
#     )
#     ProductDetailView,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView,
#     ProductDetailSlugView
#     )
from carts.views import cart_home

from .views import home_page, about, contact, login_page, register_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='login'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('carts.urls', namespace='cart')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^search/', include('search.urls', namespace='search')),
   ]

#url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)