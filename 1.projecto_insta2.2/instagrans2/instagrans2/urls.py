
from django.contrib import admin
from django.urls import path
from instagrans2.views import HomeView, LoginView, RegisterView, ContactView, LegalView, logout_view, ProfileDetailView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("legal/", LegalView.as_view(), name="legal"),
    path('profile/<pk>/', ProfileDetailView.as_view(), name="profile_detail"),
    path('admin/', admin.site.urls),
]
