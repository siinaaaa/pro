from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('home', views.Base.as_view()),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.bet),
    path("test", views.gg)

]