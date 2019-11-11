"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import HotdealView

hotdeal_list = HotdealView.as_view({
    'post':'create',
    'get':'list'
})

# urlpatterns = [
#     path('', views.hotdeal_all, name="all"),
#     # path('create/', views.hotdeal_create, name="create"),
#     path('<int:pK>/',views.hotdeal_detail, name="detail"),
#     # path('<int:pk>/update/',views.hotdeal_update, name="update"),
#     # path('<int:pk>/delete/',views.hotdeal_delete, name="delete"),
    
# ]

# 아래처럼 하면 linux에서는 인식을 못한다.
# urlpatterns = format_suffix_patterns([
#     path('hotdeal/', hotdeal_list, name='hotdeal_list'),
# ])

urlpatterns = [
    path('hotdeal/', hotdeal_list, name='hotdeal_list'),
]