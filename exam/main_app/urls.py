from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from main_app import views

urlpatterns = [
    url(r'category/$', views.shop_category_list),
    url(r'product/$', views.ProductView.as_view()),
    url(r'cart/$', views.CartView.as_view()),
    url(r'profile/register/$', views.create_user),
    url(r'profile/auth/$', obtain_jwt_token),
    url(r'profile/(?P<pk>\d+)/$', views.ProfileView.as_view()),
    url(r'profile/orders/$', views.OrderUserView.as_view()),
    url(r'order/$', views.OrderCreateView.as_view()),
    url(r'order/(?P<pk>\d+)/$', views.OrderView.as_view()),
]
