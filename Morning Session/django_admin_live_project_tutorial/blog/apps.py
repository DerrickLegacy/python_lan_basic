from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class BlognConfig(AdminConfig):
    default_site = 'blog.admin.BlogAdminArea'
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
