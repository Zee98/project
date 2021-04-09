from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_views
from rest_framework import routers

# routes for api
router = routers.DefaultRouter()
router.register(r'money', user_view.MoneyViewSet)
router.register(r'rate', user_view.ConvertionViewSet)

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="index.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('', user_view.Sign_up, name="sign_up"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))    
]
