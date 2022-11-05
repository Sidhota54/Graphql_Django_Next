from django.contrib import admin
from app.models import Store
from app.models import Columns
from app.models import CustomUser

admin.site.register(Columns)
admin.site.register(Store)
admin.site.register(CustomUser)