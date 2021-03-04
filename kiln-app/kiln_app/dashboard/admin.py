from django.contrib import admin
from dashboard.models import User, Kiln, Load, Reading
# Register your models here.
admin.site.register(User)
admin.site.register(Kiln)
admin.site.register(Load)
admin.site.register(Reading)
