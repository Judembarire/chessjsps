from django.contrib import admin
from .models import Tshirts, Hoodies, Goodies, Events

# Register your models here.

admin.site.register(Tshirts)
admin.site.register(Hoodies)
admin.site.register(Goodies)
admin.site.register(Events)
