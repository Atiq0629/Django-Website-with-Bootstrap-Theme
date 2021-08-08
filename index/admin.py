from django.contrib import admin

from .models  import about, slider, client, Musician

admin.site.register(about)
admin.site.register(slider)
admin.site.register(client)
admin.site.register(Musician)


