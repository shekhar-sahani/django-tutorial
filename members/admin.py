from django.contrib import admin

from members.models import Members

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname']
admin.site.register(Members, MemberAdmin) 