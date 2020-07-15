from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home-page'),
    path('blog/', views.BlogListView.as_view(), name='blog-page'),
    path('single/<int:pk>', views.BlogDetailView.as_view(), name='single-page'),
]
