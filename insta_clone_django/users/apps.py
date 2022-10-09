from django.apps import AppConfig

# Why the fuck did I put this class?
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'



