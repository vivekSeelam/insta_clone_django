from django.urls import path
from . import views

# localhost: 8000/users/
# localhost: 8000/users/index

urlpatterns = [
    path('', views.index, name="users_main_index"),
    path('index/', views.index, name="users_main_index"),
    path('signup/', views.signup, name="user_sign_up")
]
