from django.contrib.auth import views as authViews
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from users import views as usersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('reg/', usersView.register, name='reg'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', usersView.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
