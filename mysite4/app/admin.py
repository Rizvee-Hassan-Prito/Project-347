from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined','last_login', 'is_admin','is_staff','is_superuser','address', 'mobile_number', 'profile_pics')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)